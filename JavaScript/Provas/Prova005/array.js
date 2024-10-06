/*Você foi convidado(a) a desenvolver um aplicativo web para ajudar a gerenciar as tarefas domésticas de uma família agitada.
O objetivo é criar um "Gerenciador de Tarefas Domésticas" que permita que todos os membros da família adicionem, removam e atualizem suas tarefas diárias
garantindo que tudo seja feito de forma organizada.*/

// Para adicionar uma nova tarefa
document.addEventListener("DOMContentLoaded", function() {
    const taskList = document.getElementById("taskList");
    const addButton = document.getElementById("addButton");
    const taskInput = document.getElementById("taskInput");

    addButton.addEventListener("click", function() {
        const taskText = taskInput.value.trim();

        if (taskText !== "") {
            const li = document.createElement("li");
            li.textContent = taskText;

            // Para deletar uma tarefa
            const deleteButton = document.createElement("button");
            deleteButton.textContent = "remover";
            deleteButton.className = "delete";
            deleteButton.onclick = function() {
                taskList.removeChild(li);
            };

            // Para limpar o input
            li.appendChild(deleteButton);
            taskList.appendChild(li);
            taskInput.value = "";
        } else {
            alert("Por favor, insira uma tarefa.");
        }
    });
});
