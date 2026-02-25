import { readdir, readFile } from 'fs/promises';
import { join, basename } from 'path';
import { fileURLToPath } from 'url';
import { dirname } from 'path';

const __dirname = dirname(fileURLToPath(import.meta.url));
const SKILLS_DIR = join(__dirname, '..', 'skills');

const REQUIRED_FILES = ['SKILL.md', 'LICENSE.txt'];
const REQUIRED_FRONTMATTER_FIELDS = ['name', 'description', 'metadata'];

async function* getSkillDirectories(dir) {
  const entries = await readdir(dir, { withFileTypes: true });
  for (const entry of entries) {
    if (entry.isDirectory()) {
      yield join(dir, entry.name);
    }
  }
}

async function parseFrontmatter(content) {
  const match = content.match(/^---\n([\s\S]*?)\n---/);
  if (!match) return null;
  
  const frontmatter = {};
  const frontmatterText = match[1];
  
  const nameMatch = frontmatterText.match(/^name:\s*(.+)$/m);
  if (nameMatch) frontmatter.name = nameMatch[1].trim();
  
  const descMatch = frontmatterText.match(/^description:\s*(.+)$/m);
  if (descMatch) frontmatter.description = descMatch[1].trim();
  
  const metadataMatch = frontmatterText.match(/^metadata:/m);
  if (metadataMatch) frontmatter.metadata = {};
  
  return frontmatter;
}

async function validateSkill(skillPath) {
  const errors = [];
  const skillName = basename(skillPath);
  
  for (const requiredFile of REQUIRED_FILES) {
    try {
      await readFile(join(skillPath, requiredFile));
    } catch {
      errors.push(`Missing required file: ${requiredFile}`);
    }
  }
  
  try {
    const skillMdContent = await readFile(join(skillPath, 'SKILL.md'), 'utf-8');
    const frontmatter = await parseFrontmatter(skillMdContent);
    
    if (!frontmatter) {
      errors.push('Missing YAML frontmatter in SKILL.md');
    } else {
      for (const field of REQUIRED_FRONTMATTER_FIELDS) {
        if (!frontmatter[field]) {
          errors.push(`Missing frontmatter field: ${field}`);
        }
      }
    }
  } catch (e) {
    errors.push(`Error reading SKILL.md: ${e.message}`);
  }
  
  return errors;
}

async function findAllSkills() {
  const skills = [];
  const categories = ['.system', '.curated'];
  
  for (const category of categories) {
    const categoryPath = join(SKILLS_DIR, category);
    try {
      for await (const skillDir of getSkillDirectories(categoryPath)) {
        skills.push({ path: skillDir, category });
      }
    } catch {
      // Category might not exist
    }
  }
  
  return skills;
}

async function runTests() {
  const skills = await findAllSkills();
  let passed = 0;
  let failed = 0;
  
  console.log(`\nValidating ${skills.length} skills...\n`);
  
  for (const skill of skills) {
    const errors = await validateSkill(skill.path);
    const skillName = basename(skill.path);
    
    if (errors.length === 0) {
      console.log(`✓ ${skill.category}/${skillName}: Valid`);
      passed++;
    } else {
      console.log(`✗ ${skill.category}/${skillName}:`);
      for (const error of errors) {
        console.log(`  - ${error}`);
      }
      failed++;
    }
  }
  
  console.log(`\n=== Results ===`);
  console.log(`Passed: ${passed}`);
  console.log(`Failed: ${failed}`);
  
  if (failed > 0) {
    process.exit(1);
  }
}

runTests().catch(console.error);
