function numeroFatorial(n){
   if (n === 0 || n === 1) {
       return 1;
   }
   
   let resultado = 1;

   for (let i = 2; i <= n; i++) {
       resultado *= i;
       console.log(`Passo ${i-1}: ${resultado}`);
   }
   
   return resultado;
}

console.log(`Resultado final: ${numeroFatorial(10)}`);