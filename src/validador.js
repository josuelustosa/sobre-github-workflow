// Conjunto de REGEX para validação de entradas.

function validar_email(email)
{
    if(/^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/.test(email)){
        return true;
    }else return false;
 
}
  
function validar_cep(cep){
      if(/^[0-9]{5}-[0-9]{3}$/.test(cep)){
        return true;
    }else return false;

}

function validar_cpf(cpf){
    if(/^\d{3}\.\d{3}\.\d{3}\-\d{2}$/.test(cpf)){
        return true;
    }else return false;

}

function validar_telefone(telefone){
    if(/[0-9]{2}-([0-9]{8}|[0-9]{9})$/.test(telefone)){
        return true;
    }else return 'telefone invalido';

}

console.log(validar_cpf('053.340.532-00'));
console.log(validar_email('joao.maciel.br@gmail.com.br'));
console.log(validar_telefone('92-981016231'));
console.log(validar_cep('69054-666'));
