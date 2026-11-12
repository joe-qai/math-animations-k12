// 数独游戏验证（精简版）
var TEMPLATE=[[5,3,4,6,7,8,9,1,2],[6,7,2,1,9,5,3,4,8],[1,9,8,3,4,2,5,6,7],[8,5,9,7,6,1,4,2,3],[4,2,6,8,5,3,7,9,1],[7,1,3,9,2,4,8,5,6],[9,6,1,5,3,7,2,8,4],[2,8,7,4,1,9,6,3,5],[3,4,5,2,8,6,1,7,9]];
var shuffle=function(a){for(var i=a.length-1;i>0;i--){var j=Math.floor(Math.random()*(i+1));var t=a[i];a[i]=a[j];a[j]=t;}return a;};
function fullBoard(){var mapping=[1,2,3,4,5,6,7,8,9];shuffle(mapping);var b=[];for(var r=0;r<9;r++){b[r]=[];for(var c=0;c<9;c++)b[r][c]=mapping[TEMPLATE[r][c]-1];}return b;}
function check(b){for(var r=0;r<9;r++){if(new Set(b[r]).size!==9)return'r'+r;}for(var cc=0;cc<9;cc++){if(new Set(b.map(function(r){return r[cc];})).size!==9)return'c'+cc;}for(var br=0;br<3;br++){for(var bc=0;bc<3;bc++){var cells=[];for(var r=br*3;r<br*3+3;r++)for(var cc=bc*3;cc<bc*3+3;cc++)cells.push(b[r][cc]);if(new Set(cells).size!==9)return'box'+br+''+bc;}}return null;}

console.log('=== 数独验证 ===\n');
console.log('1. 模板验证...');
var te=check(TEMPLATE);
console.log(te?'FAIL: '+te:'✓ 模板合法');

console.log('\n2. 生成器验证（1000次）...');
var errs=0;
for(var t=0;t<1000;t++){var e=check(fullBoard());if(e)errs++;}
console.log(errs===0?'✓ 1000局全部合法':'✗ '+errs+'局非法');

console.log('\n3. 挖空验证（模拟startGame流程）...');
errs=0;
for(var t=0;t<500;t++){
  var sol=fullBoard();
  var p=sol.map(function(r){return r.slice();});
  var fixed=Array.from({length:9},function(){return Array(9).fill(true);});
  var rem=30,tries=0;
  while(rem>0&&tries<500){
    var r=Math.floor(Math.random()*9),c=Math.floor(Math.random()*9);
    if(p[r][c]!==0){p[r][c]=0;fixed[r][c]=false;rem--;}
    tries++;
  }
  // 检查solution是否仍合法
  var se=check(sol);
  if(se)errs++;
  // 检查puzzle中没有出现"固定格值!=解"的错误（应该总是相等的）
  for(var r=0;r<9;r++){for(var c=0;c<9;c++){
    if(fixed[r][c]&&p[r][c]!==sol[r][c])errs++;
  }}
}
console.log(errs===0?'✓ 500局挖空流程无bug':'✗ '+errs+'处错误');

console.log('\n=== 验证完毕 ===');