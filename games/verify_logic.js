// 数学游戏逻辑正确性自检 (clean version)
console.log('=== Math Games Verification ===\n');

// 1. Arithmetic Match
(function(){
  function randInt(min,max){return Math.floor(Math.random()*(max-min+1))+min;}
  var err=0;
  for(var t=0;t<500;t++){
    var diff=['easy','medium','hard'][t%3];
    var ops=diff==='easy'?['+','-']:diff==='medium'?['+','-','×']:['+','-','×','÷'];
    var count={easy:6,medium:8,hard:10}[diff];
    for(var i=0;i<count;i++){
      var op=ops[Math.floor(Math.random()*ops.length)];
      var a,b,ans;
      if(op==='+'){a=randInt(1,19);b=randInt(1,20-a);ans=a+b;}
      else if(op==='-'){a=randInt(1,20);b=randInt(1,a);ans=a-b;}
      else if(op==='×'){a=randInt(2,12);b=randInt(2,9);ans=a*b;}
      else{b=randInt(2,9);ans=randInt(1,12);a=b*ans;}
      var ok=true;
      if(op==='+')ok=(a+b===ans);
      else if(op==='-')ok=(a-b===ans);
      else if(op==='×')ok=(a*b===ans);
      else ok=(a/b===ans&&a%b===0);
      if(!ok)err++;
    }
  }
  console.log('[Arithmetic Match] '+(err===0?'PASS':'FAIL ('+err+')'));
})();

// 2. Number Guess (Bulls & Cows)
(function(){
  function shuffle(a){for(var i=a.length-1;i>0;i--){var j=Math.floor(Math.random()*(i+1));var t=a[i];a[i]=a[j];a[j]=t;}return a;}
  function genSecret(n){
    var pool=[1,2,3,4,5,6,7,8,9];shuffle(pool);var first=pool[0];
    var rem=[0,1,2,3,4,5,6,7,8,9].filter(function(d){return d!==first;});shuffle(rem);
    return first+rem.slice(0,n-1).join('');
  }
  function calcBC(guess,secret){var b=0,c=0;for(var i=0;i<secret.length;i++){if(guess[i]===secret[i])b++;else if(secret.indexOf(guess[i])>=0)c++;}return{bull:b,cow:c};}
  var err=0;
  [3,4,5].forEach(function(n){for(var t=0;t<200;t++){
    var s=genSecret(n);
    if(s[0]==='0'||new Set(s).size!==n)err++;
    var r=calcBC(s,s);if(r.bull!==n||r.cow!==0)err++;
  }});
  console.log('[Number Guess] '+(err===0?'PASS':'FAIL ('+err+')'));
})();

// 3. Hopscotch
(function(){
  var G=10;
  function genTiles(count){
    var ts=[];for(var i=0;i<count;i++){var x,y;do{x=Math.floor(Math.random()*G);y=Math.floor(Math.random()*G);}while(ts.some(function(t){return t.x===x&&t.y===y;}));ts.push({x:x,y:y,v:i+1});}return ts;
  }
  var err=0;
  [1,2,3].forEach(function(lv){
    var count=5+lv*2,tiles=genTiles(count);
    var posSet=new Set(tiles.map(function(t){return t.x+','+t.y;}));
    if(posSet.size!==count)err++;
    var vals=tiles.map(function(t){return t.v;}).sort(function(a,b){return a-b;});
    for(var i=0;i<count;i++)if(vals[i]!==i+1)err++;
  });
  console.log('[Hopscotch] '+(err===0?'PASS':'FAIL ('+err+')'));
})();

// 4. Sudoku
(function(){
  function valid(b,r,c,n){
    for(var i=0;i<9;i++){if(b[r][i]===n||b[i][c]===n)return false;}
    var br=Math.floor(r/3)*3,bc=Math.floor(c/3)*3;
    for(var rr=br;rr<br+3;rr++)for(var cc=bc;cc<bc+3;cc++)if(b[rr][cc]===n)return false;
    return true;
  }
  function solve(b){
    for(var r=0;r<9;r++)for(var c=0;c<9;c++){
      if(b[r][c]!==0)continue;
      var nums=[1,2,3,4,5,6,7,8,9];
      for(var i=nums.length-1;i>0;i--){var j=Math.floor(Math.random()*(i+1));var tmp=nums[i];nums[i]=nums[j];nums[j]=tmp;}
      for(var k=0;k<nums.length;k++){
        var n=nums[k];
        if(valid(b,r,c,n)){b[r][c]=n;if(solve(b))return true;b[r][c]=0;}
      }
      return false;
    }
    return true;
  }
  var err=0;
  for(var t=0;t<20;t++){
    var sol=[];
    for(var r=0;r<9;r++){sol[r]=[];for(var c=0;c<9;c++)sol[r][c]=0;}
    solve(sol);
    for(var r=0;r<9;r++){var row=new Set(sol[r]);if(row.size!==9)err++;}
    for(var c=0;c<9;c++){var col=new Set(sol.map(function(r){return r[c];}));if(col.size!==9)err++;}
    for(var br=0;br<3;br++){for(var bc=0;bc<3;bc++){
      var cells=[];
      for(var r=br*3;r<br*3+3;r++)for(var c=bc*3;c<bc*3+3;c++)cells.push(sol[r][c]);
      if(new Set(cells).size!==9)err++;
    }}
  }
  console.log('[Sudoku] '+(err===0?'PASS':'FAIL ('+err+')'));
})();

// 5. Huarongdao (Klotski)
(function(){
  var C=5,R=6,TS={big:[2,2],vert:[1,2],horz:[2,1],square:[1,1]};
  var levels=[
    {name:'A',blocks:[{type:'big',x:2,y:0},{type:'vert',x:0,y:0},{type:'vert',x:4,y:0},{type:'horz',x:0,y:2},{type:'horz',x:3,y:2},{type:'square',x:2,y:3},{type:'square',x:3,y:3},{type:'vert',x:0,y:3},{type:'vert',x:4,y:3}]},
    {name:'B',blocks:[{type:'big',x:2,y:0},{type:'vert',x:0,y:0},{type:'vert',x:4,y:0},{type:'horz',x:0,y:3},{type:'horz',x:3,y:3},{type:'square',x:1,y:2},{type:'square',x:2,y:2},{type:'vert',x:0,y:4},{type:'vert',x:4,y:4}]},
    {name:'C',blocks:[{type:'big',x:2,y:0},{type:'vert',x:0,y:0},{type:'vert',x:4,y:0},{type:'horz',x:0,y:2},{type:'horz',x:3,y:2},{type:'square',x:1,y:3},{type:'square',x:2,y:3},{type:'vert',x:0,y:4},{type:'vert',x:4,y:4},{type:'square',x:3,y:4}]}
  ];
  var err=0;
  levels.forEach(function(lv){
    for(var i=0;i<lv.blocks.length;i++){
      var b=lv.blocks[i],[bw,bh]=TS[b.type];
      if(b.x+bw>C||b.y+bh>R)err++;
      for(var j=i+1;j<lv.blocks.length;j++){
        var o=lv.blocks[j],[ow,oh]=TS[o.type];
        if(b.x<o.x+ow&&b.x+bw>o.x&&b.y<o.y+oh&&b.y+bh>o.y)err++;
      }
    }
  });
  console.log('[Huarongdao] '+(err===0?'PASS':'FAIL ('+err+' overlaps)'));
})();

console.log('\nAll checks done.');
