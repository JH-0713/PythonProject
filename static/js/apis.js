async function getGato() {
    let resultado=await fetch("https://api.thecatapi.com/v1/images/search")

    if (resultado.ok) {
        let dados = await resultado.json()
        render_gato(dados)
    }
}

function render_gato(dados) {
    let urlImg_g = dados[0].url
    const imgGato = document.getElementById('img-gato')
    const iconGato = document.getElementById('icon-gato')

    iconGato.style.display = "none"
    imgGato.style.display = "block"
    imgGato.src = urlImg_g

}

async function detDog() {
    let resultado=await fetch("https://dog.ceo/api/breeds/image/random")

    if (resultado.ok) {
        let dados = await resultado.json()
        render_dog(dados)
    }
}

function render_dog(dados) {
    let urlImg_d = dados[0].message
    const imgDog = document.getElementById('img-dog')
    const iconDog = document.getElementById('icon-dog')

    iconDog.style.display = "none"
    imgDog.style.display = "block"
    imgDog.src = urlImg_d

}

async function getFox() {
    let resultado=await fetch("https://randomfox.ca/floof")

    if (resultado.ok) {
        let dados = await resultado.json()
        render_gato(dados)
    }
}

function render_fox(dados) {
    let urlImg_f = dados[0].image
    const imgFox = document.getElementById('img-fox')
    const iconFox = document.getElementById('icon-fox')

    iconFox.style.display = "none"
    imgFox.style.display = "block"
    imgFox.src = urlImg_f

}
