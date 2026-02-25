#!/usr/bin/env node

const fs = require('fs');
const path = require('path');

const SKILLS_DIR = path.join(__dirname, '..', 'skills');

function getCategory(skillPath) {
  if (skillPath.includes('/.system/')) return '.system';
  if (skillPath.includes('/.curated/')) return '.curated';
  if (skillPath.includes('/.experimental/')) return '.experimental';
  return '.curated';
}

function extractFrontmatter(content) {
  const match = content.match(/^---\n([\s\S]*?)\n---/);
  if (!match) return {};
  
  const frontmatter = {};
  const lines = match[1].split('\n');
  
  for (const line of lines) {
    const colonIdx = line.indexOf(':');
    if (colonIdx === -1) continue;
    
    const key = line.slice(0, colonIdx).trim();
    let value = line.slice(colonIdx + 1).trim();
    
    if (value.startsWith('"') && value.endsWith('"')) {
      value = value.slice(1, -1);
    }
    
    frontmatter[key] = value;
  }
  
  return frontmatter;
}

function extractOpenAIYaml(content) {
  const result = {};
  
  const displayMatch = content.match(/display_name:\s*"([^"]+)"/);
  if (displayMatch) result.display_name = displayMatch[1];
  
  const shortDescMatch = content.match(/short_description:\s*"([^"]+)"/);
  if (shortDescMatch) result.short_description = shortDescMatch[1];
  
  return result;
}

function getLicense(skillPath) {
  const licensePath = path.join(skillPath, 'LICENSE.txt');
  if (fs.existsSync(licensePath)) {
    return 'See LICENSE.txt';
  }
  return 'MIT';
}

function findSkills() {
  const categories = ['.system', '.curated', '.experimental'];
  const skills = [];
  
  for (const category of categories) {
    const categoryPath = path.join(SKILLS_DIR, category);
    if (!fs.existsSync(categoryPath)) continue;
    
    const entries = fs.readdirSync(categoryPath);
    for (const entry of entries) {
      const skillPath = path.join(categoryPath, entry);
      const stat = fs.statSync(skillPath);
      if (stat.isDirectory()) {
        skills.push({ name: entry, path: skillPath, category });
      }
    }
  }
  
  return skills;
}

function generateSkillJson(skill) {
  const skillMdPath = path.join(skill.path, 'SKILL.md');
  const openaiYamlPath = path.join(skill.path, 'agents', 'openai.yaml');
  
  let name = skill.name;
  let description = '';
  
  if (fs.existsSync(skillMdPath)) {
    const content = fs.readFileSync(skillMdPath, 'utf8');
    const frontmatter = extractFrontmatter(content);
    if (frontmatter.name) name = frontmatter.name;
    if (frontmatter.description) description = frontmatter.description;
  }
  
  let displayName = name;
  if (fs.existsSync(openaiYamlPath)) {
    const yamlContent = fs.readFileSync(openaiYamlPath, 'utf8');
    const yamlData = extractOpenAIYaml(yamlContent);
    if (yamlData.display_name) displayName = yamlData.display_name;
    if (!description && yamlData.short_description) {
      description = yamlData.short_description;
    }
  }
  
  if (!description) {
    description = `${name} skill for Codex`;
  }
  
  if (description.length > 200) {
    description = description.slice(0, 197) + '...';
  }
  
  const skillJson = {
    name,
    version: '1.0.0',
    description,
    category: skill.category,
    author: {
      name: 'Codex Community',
      url: 'https://github.com/kommas02/skills'
    },
    capabilities: [],
    dependencies: [],
    tags: [name.split('-')[0]],
    license: getLicense(skill.path),
    homepage: `https://github.com/kommas02/skills/tree/main/skills/${skill.category}/${name}`,
    repository: 'https://github.com/kommas02/skills'
  };
  
  return skillJson;
}

function main() {
  console.log('Migrating skills to skill.json format...\n');
  
  const skills = findSkills();
  console.log(`Found ${skills.length} skills\n`);
  
  const force = process.argv.includes('--force');
  
  for (const skill of skills) {
    const skillJsonPath = path.join(skill.path, 'skill.json');
    
    if (fs.existsSync(skillJsonPath) && !force) {
      console.log(`  SKIP: ${skill.name} (skill.json already exists)`);
      continue;
    }
    
    const skillJson = generateSkillJson(skill);
    fs.writeFileSync(skillJsonPath, JSON.stringify(skillJson, null, 2) + '\n');
    console.log(`  CREATE: ${skill.name}`);
  }
  
  console.log('\nMigration complete!');
}

main();
