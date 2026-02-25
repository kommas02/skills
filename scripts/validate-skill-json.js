#!/usr/bin/env node

const fs = require('fs');
const path = require('path');

const SKILLS_DIR = path.join(__dirname, '..', 'skills');

const schema = {
  type: 'object',
  required: ['name', 'version', 'description', 'category'],
  properties: {
    name: { type: 'string', pattern: '^[a-z0-9-]+$' },
    version: { type: 'string', pattern: '^[0-9]+\\.[0-9]+\\.[0-9]+$' },
    description: { type: 'string', minLength: 10, maxLength: 200 },
    category: { type: 'string', enum: ['.system', '.curated', '.experimental'] },
    author: { type: 'object' },
    capabilities: { type: 'array' },
    dependencies: { type: 'array' },
    tags: { type: 'array' },
    license: { type: 'string' },
    homepage: { type: 'string' },
    repository: { type: 'string' }
  }
};

function getCategory(skillPath) {
  if (skillPath.includes('/.system/')) return '.system';
  if (skillPath.includes('/.curated/')) return '.curated';
  if (skillPath.includes('/.experimental/')) return '.experimental';
  return null;
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

function validateString(value, pattern) {
  if (typeof value !== 'string') return false;
  if (pattern) {
    const regex = new RegExp(pattern);
    return regex.test(value);
  }
  return true;
}

function validateSkillJson(skillJson, skillName) {
  const errors = [];
  
  if (!skillJson.name) errors.push('missing name');
  else if (!validateString(skillJson.name, '^[a-z0-9-]+$')) errors.push('invalid name format');
  
  if (!skillJson.version) errors.push('missing version');
  else if (!validateString(skillJson.version, '^[0-9]+\\.[0-9]+\\.[0-9]+$')) errors.push('invalid version format');
  
  if (!skillJson.description) errors.push('missing description');
  else if (skillJson.description.length < 10 || skillJson.description.length > 200) errors.push('description length out of range');
  
  if (!skillJson.category) errors.push('missing category');
  else if (!['.system', '.curated', '.experimental'].includes(skillJson.category)) errors.push('invalid category');
  
  return errors;
}

function main() {
  console.log('Validating skill.json files...\n');
  
  const skills = findSkills();
  let hasErrors = false;
  
  for (const skill of skills) {
    const skillJsonPath = path.join(skill.path, 'skill.json');
    
    if (!fs.existsSync(skillJsonPath)) {
      console.log(`  ERROR: ${skill.name} - skill.json not found`);
      hasErrors = true;
      continue;
    }
    
    try {
      const content = fs.readFileSync(skillJsonPath, 'utf8');
      const skillJson = JSON.parse(content);
      const errors = validateSkillJson(skillJson, skill.name);
      
      if (errors.length > 0) {
        console.log(`  ERROR: ${skill.name} - ${errors.join(', ')}`);
        hasErrors = true;
      } else {
        console.log(`  OK: ${skill.name}`);
      }
    } catch (e) {
      console.log(`  ERROR: ${skill.name} - invalid JSON`);
      hasErrors = true;
    }
  }
  
  if (hasErrors) {
    console.log('\nValidation FAILED');
    process.exit(1);
  } else {
    console.log('\nValidation PASSED');
    process.exit(0);
  }
}

main();
