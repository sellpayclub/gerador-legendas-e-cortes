// Source migration/audit tool. No DOM rewriting, translation service or user text.
const fs = require('node:fs');
const path = require('node:path');
const ts = require('../frontend/node_modules/typescript');
const root = path.resolve(__dirname, '../frontend');
require.extensions['.ts'] = (module, file) => module._compile(ts.transpileModule(fs.readFileSync(file, 'utf8'), {compilerOptions:{module:ts.ModuleKind.CommonJS}}).outputText, file);
const {copyCatalog} = require('../frontend/lib/i18n/copy.ts');
const keys = new Set(Object.keys(copyCatalog));
const audit = [];
function run(file) {
  let code = fs.readFileSync(file,'utf8');
  const sf = ts.createSourceFile(file,code,ts.ScriptTarget.Latest,true,file.endsWith('tsx')?ts.ScriptKind.TSX:ts.ScriptKind.TS);
  const edits=[]; let used=false;
  const normalized = text => text.replace(/\s+/g,' ').trim();
  function replace(n,text){edits.push([n.getStart(sf),n.end,text]);used=true;}
  function insideFunction(n){for(let p=n.parent;p;p=p.parent) if(ts.isFunctionLike(p)) return true; return false;}
  function walk(n){
    // Preserve already localized strings, internal comparisons and state keys.
    if(ts.isCallExpression(n) && ['copy','t','translate'].includes(n.expression.getText(sf)))return;
    if(ts.isCallExpression(n) && ts.isPropertyAccessExpression(n.expression) && ['includes','startsWith','endsWith'].includes(n.expression.name.text)) return;
    if(ts.isTemplateExpression(n)) {
      let key=n.head.text;const params=[];
      n.templateSpans.forEach((span,i)=>{key+=`{${i}}`+span.literal.text;params.push(`${JSON.stringify(i)}: ${span.expression.getText(sf)}`)});
      if(keys.has(normalized(key))){replace(n,`copy(${JSON.stringify(key)}, {${params.join(', ')}})`);return;}
    }
    if(ts.isJsxText(n)){
      const text=normalized(n.text);
      if(keys.has(text)) replace(n,`{copy(${JSON.stringify(text)})}`);
      else if(/[A-Za-zÀ-ÿ]/.test(text)) audit.push({file:path.relative(root,file),text});
      return;
    }
    if(ts.isStringLiteral(n)||ts.isNoSubstitutionTemplateLiteral(n)){
      const text=normalized(n.text);const p=n.parent;
      if(keys.has(text)){
        if(ts.isJsxAttribute(p)) {
          if(['title','placeholder','alt','aria-label','label','description','hint'].includes(p.name.getText(sf)))replace(n,`{copy(${JSON.stringify(n.text)})}`);
        } else if(ts.isPropertyAssignment(p)&&p.name===n){} // object keys
        else if(ts.isBinaryExpression(p)&&[ts.SyntaxKind.EqualsEqualsEqualsToken,ts.SyntaxKind.ExclamationEqualsEqualsToken].includes(p.operatorToken.kind)){}
        else if(!insideFunction(n)&&ts.isPropertyAssignment(p)) replace(p,`get ${p.name.getText(sf)}() { return copy(${JSON.stringify(n.text)}); }`);
        else if(insideFunction(n))replace(n,`copy(${JSON.stringify(n.text)})`);
      }else if(/[áàãâéêíóôõúç]/i.test(text))audit.push({file:path.relative(root,file),text});
      return;
    }
    ts.forEachChild(n,walk);
  }
  walk(sf);
  if(used && process.argv.includes('--write')) {
    for(const [start,end,replacement] of edits.sort((a,b)=>b[0]-a[0]))code=code.slice(0,start)+replacement+code.slice(end);
    const client=code.startsWith('"use client"');
    const offset=client?code.indexOf(';')+1:0;
    if(!code.includes('import { copy }'))code=code.slice(0,offset)+ '\nimport { copy } from "@/lib/i18n/copy";\n'+code.slice(offset);
    // Subscribe each component to locale changes; copy is also usable by
    // event handlers and module-level option getters without calling hooks.
    if(client && !code.includes('useLocaleSubscription')){
      let changed=ts.createSourceFile(file,code,99,true,ts.ScriptKind.TSX);let insert=[];
      function subscribe(n){if(ts.isFunctionDeclaration(n)&&n.name&&/^[A-Z]/.test(n.name.text)&&n.body)insert.push(n.body.getStart(changed)+1);ts.forEachChild(n,subscribe)}subscribe(changed);
      for(const pos of insert.sort((a,b)=>b-a))code=code.slice(0,pos)+'\n  useLocaleSubscription();'+code.slice(pos);
      if(insert.length)code=code.slice(0,offset)+'\nimport { useI18n as useLocaleSubscription } from "@/lib/i18n/context";\n'+code.slice(offset);
    }
    fs.writeFileSync(file,code);
  }
}
function walk(dir){for(const name of fs.readdirSync(dir)){const file=path.join(dir,name);if(fs.statSync(file).isDirectory()){if(!file.includes('/i18n'))walk(file);}else if(/\.(ts|tsx)$/.test(file)&&!file.endsWith('layout.tsx'))run(file);}}
for(const dir of ['app','components','lib'])walk(path.join(root,dir));
console.log(JSON.stringify(audit,null,2));
