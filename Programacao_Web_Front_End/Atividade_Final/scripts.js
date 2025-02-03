function getById(id) {
    return document.getElementById(id);
}

document.addEventListener("DOMContentLoaded", async () => {
    try {
        // Buscar posts
        const postResponse = await fetch("https://jsonplaceholder.typicode.com/posts");
        const posts = await postResponse.json();

        // Buscar usuários
        const userResponse = await fetch("https://jsonplaceholder.typicode.com/users");
        const users = await userResponse.json();

        // Criar um mapa de usuários (id -> nome)
        const userMap = {};
        users.forEach(user => {
            userMap[user.id] = { name: user.name, email: user.email };
        });

        // Substituir userId pelo nome do usuário
        const conteudoBlogPost = document.getElementById("conteudoBlogPost");
        posts.forEach(post => {
            const user = userMap[post.userId] || { name: "Desconhecido", email: "N/A" };
            const postElement = document.createElement("div");
            postElement.classList.add("post");
            postElement.innerHTML = `
                <p class="user">${user.name}</p>
                <span class="email">${user.email}</span>
                <p>${post.body}</p>
                <a class="comentarioLink" onclick="mostrarComentarios(${post.id})">Ver Comentários</a>
            `;
            conteudoBlogPost.appendChild(postElement);
        });

    } catch (error) {
        console.error("Erro ao buscar dados:", error);
    }
});

async function mostrarComentarios(postId) {
    try {
        const comentariosResponse = await fetch(`https://jsonplaceholder.typicode.com/comments?postId=${postId}`);
        const comentarios = await comentariosResponse.json();

        let comentariosHTML = `<h2>Comentários do Post ${postId}</h2>`;
        comentarios.forEach(comentario => {
            comentariosHTML += `<p><strong>${comentario.name}</strong>: ${comentario.body}</p>`;
        });

        const popup = window.open("", "_blank", "width=400,height=400");
        popup.document.write(`<html><head><title>Comentários</title></head><body>${comentariosHTML}</body></html>`);
        popup.document.close();
    } catch (error) {
        console.error("Erro ao buscar comentários:", error);
    }
};