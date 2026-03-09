// let nome = prompt('Como vc chama?')
//
// == Verifica o valor ex: 'JH' == ''
// === Verifica o tipo e valor ex: 'JH' tipo:"string" === '' tipo:"string"
// == VERIFICA O VALOR EX: 1 == '1' irá ser igual
//
// if (nome == null) {
//     alert('Recarregue a página')
// } else {
//     let correto = confirm(`Voce se chama ${nome}?`)
//
//     if (correto) {
//         alert(` ${nome} Bem vindo ao site de cursos`) // ou nome + 'Texto' == nome Texto//
//     } else {
//         alert('Recarregue a página')
//     }
// }

function limpaInputsCad() {
    const inputNome = document.getElementById('input-name')
    const inputData = document.getElementById('input-date')
    const inputCpf = document.getElementById('input-cpf')
    const inputEmail_ = document.getElementById('input-email')
    const inputSenha_ = document.getElementById('input-senha')
    const inputCargo = document.getElementById('input-cargo')
    const inputSalarie = document.getElementById('input-salario')

    inputNome.value = ''
    inputData.value = ''
    inputCpf.value = ''
    inputEmail_.value = ''
    inputSenha_.value = ''
    inputCargo.value = ''
    inputSalarie.value = ''
}

function limpaInputsLogin() {
    const inputEmail = document.getElementById('input-email')
    const inputSenha = document.getElementById('input-senha')

    inputEmail.value = ''
    inputSenha.value = ''
}

document.addEventListener("DOMContentLoaded", function () {
    const formLogin = document.getElementById('form-login')

    formLogin.addEventListener('submit', function (event) {
        // Pegar 2 Inputs do Formulario
        const inputEmail = document.getElementById('input-email')
        const inputSenha = document.getElementById('input-senha')

        let temErro = false

        // Verificar se os inputs estao vazios

        if (inputEmail.value === '') {
            inputEmail.classList.add('is-invalid')
            temErro = true
        } else {
            inputEmail.classList.remove('is-invalid')
        }

        if (inputSenha.value === '') {
            inputSenha.classList.add('is-invalid')
            temErro = true
        } else {
            inputSenha.classList.remove('is-invalid')
        }

        if (temErro) {
            // evita de enviar o formulario
            event.preventDefault()
            alert('Preencha todos os campos')
        }

    })


    const formCadastrar = document.getElementById('form-cad')

    formCadastrar.addEventListener('submit', function (event) {
        // Pegar 2 Inputs do Formulario
        const inputNome = document.getElementById('i-name')
        const inputData = document.getElementById('i-date')
        const inputCpf = document.getElementById('i-cpf')
        const inputEmail_ = document.getElementById('i-email')
        const inputSenha_ = document.getElementById('i-senha')
        const inputCargo = document.getElementById('i-cargo')
        const inputSalarie = document.getElementById('i-salario')

        let temErro = false

        // Verificar se os inputs estao vazios

        if (inputNome.value === '') {
            inputNome.classList.add('is-invalid')
            temErro = true
        } else {
            inputNome.classList.remove('is-invalid')
        }

        if (inputData.value === '') {
            inputData.classList.add('is-invalid')
            temErro = true
        } else {
            inputData.classList.remove('is-invalid')
        }

        if (inputCpf.value === '') {
            inputCpf.classList.add('is-invalid')
            temErro = true
        } else {
            inputCpf.classList.remove('is-invalid')
        }

        if (inputEmail_.value === '') {
            inputEmail_.classList.add('is-invalid')
            temErro = true
        } else {
            inputEmail_.classList.remove('is-invalid')
        }

        if (inputSenha_.value === '') {
            inputSenha_.classList.add('is-invalid')
            temErro = true
        }

        else {
            inputSenha_.classList.remove('is-invalid')
        }

        if (inputCargo.value === '') {
            inputCargo.classList.add('is-invalid')
            temErro = true
        } else {
            inputCargo.classList.remove('is-invalid')
        }

        if (inputSalarie.value === '') {
            inputSalarie.classList.add('is-invalid')
            temErro = true
        } else {
            inputSalarie.classList.remove('is-invalid')
        }

        if (temErro) {
            // evita de enviar o formulario
            event.preventDefault()
            alert('Preencha todos os campos')
        }

    })
})

