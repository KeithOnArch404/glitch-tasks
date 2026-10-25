document.addEventListener("DOMContentLoaded", () => {
    const title = document.querySelector("h1");
    if (title) {
        setInterval(() => {
            title.style.textShadow = `${Math.random()*4-2}px 0 #ff00ff, ${Math.random()*4-2}px 0 #00ffff`;
            setTimeout(() => title.style.textShadow = "none", 100);
        }, 2000);
    }

    const progress = document.querySelector(".progress-bar");
    if (progress) {
        const finalWidth = progress.style.width;
        progress.style.width = "0%";
        setTimeout(() => {
            progress.style.transition = "width 1s ease";
            progress.style.width = finalWidth;
        }, 300);
    }

    // EDITAR inline
    document.querySelectorAll("li").forEach(li => {
        const textSpan = li.querySelector(".task-text");
        const editInput = li.querySelector(".edit-input");
        const editBtn = li.querySelector(".edit-btn");
        const saveForm = li.querySelector(".save-form");
        const hiddenInput = li.querySelector(".hidden-save-input");

        editBtn.addEventListener("click", () => {
            if (editInput.style.display === "none") {
                textSpan.style.display = "none";
                editInput.style.display = "block";
                editInput.focus();
                editBtn.textContent = "Cancelar";
                saveForm.style.display = "block";
            } else {
                textSpan.style.display = "block";
                editInput.style.display = "none";
                saveForm.style.display = "none";
                editBtn.textContent = "Editar";
            }
        });

        saveForm.addEventListener("submit", () => {
            hiddenInput.value = editInput.value;
        });
    });

    // Guardar posición del scroll antes de recargar
    document.querySelectorAll(".action-form").forEach(form => {
        form.addEventListener("submit", () => {
            localStorage.setItem("scrollPos", window.scrollY);
        });
    });

    const savedScroll = localStorage.getItem("scrollPos");
    if (savedScroll) {
        window.scrollTo(0, parseInt(savedScroll));
        localStorage.removeItem("scrollPos");
    }
});
