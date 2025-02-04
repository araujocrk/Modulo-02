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

        // Criar um mapa de usuários (id -> nome, email)
        const userMap = {};
        users.forEach(user => {
            userMap[user.id] = { name: user.name, email: user.email };
        });

        // Criar os posts
        const containerPosts = document.getElementById("containerPosts");
        posts.forEach(post => {
            const user = userMap[post.userId] || { name: "Desconhecido", email: "N/A" };
            const postElement = document.createElement("div");
            postElement.classList.add("post");
            postElement.innerHTML = `
                <p class="username">${user.name}</p>
                <span class="email">${user.email}</span>
                <p class="body">${post.body}</p>
                <a class="comentarioLink" onclick="mostrarComentarios(${post.id})">Ver Comentários</a>
            `;
            containerPosts.appendChild(postElement);
        });

    } catch (error) {
        console.error("Erro ao buscar dados:", error);
    }
});

async function mostrarComentarios(postId) {
    try {
        // Buscar comentários
        const comentariosResponse = await fetch(`https://jsonplaceholder.typicode.com/comments?postId=${postId}`);
        const comentarios = await comentariosResponse.json();

        // Exibir comentários em uma nova janela
        let comentariosHTML = `<h2>Comentários do Post ${postId}</h2>`;
        comentarios.forEach(comentario => {
            comentariosHTML += `<p class="comentario"><strong>${comentario.email}</strong>: ${comentario.body}</p>`;
        });

        const popup = window.open("", "_blank", "width=500,height=500");
        popup.document.write(` 
                            <html>
                            <head>
                            <title>Comentários</title>
                            <style>
                            body {
                                background-color: #DAC0A7;
                                color: #745f51;
                                font-family: 'Trebuchet MS', 'Lucida Sans Unicode', 'Lucida Grande', 'Lucida Sans', Arial, sans-serif;
                            }
                            .comentario {
                                color: black;
                                border-bottom: 0.2px solid #635348;
                                padding: 15px;
                            }
                            </style>
                            </head>
                            <body>
                            ${comentariosHTML}
                            </body>
                            </html>`
        );
        popup.document.close();
    } catch (error) {
        console.error("Erro ao buscar comentários:", error);
    }
};