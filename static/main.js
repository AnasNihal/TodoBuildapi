  function getCSRFToken() {
    return document.querySelector('meta[name="csrf-token"]').getAttribute('content');
}

fetch('http://127.0.0.1:8000/apitodo/')
    .then(response => response.json())
    .then(todos => {
        const container = document.getElementById('x');
        container.innerHTML = ''; // clear previous content

        for (let i of todos) {
            container.innerHTML += `
                <div class="flex items-start bg-slate-700/50 p-4 rounded-lg transition-all duration-300" id="todo-${i.id}">
                    <input type="checkbox" class="mt-1 form-checkbox h-5 w-5 text-green-500 bg-slate-600 border-slate-500 rounded focus:ring-green-500 cursor-pointer">
                    
                   <div class="ml-4 flex-grow">
                    <div class="flex flex-col space-y-1">
                        <input id="title-${i.id}" class="font-semibold text-gray-300 bg-transparent outline-none" value="${i.title}" disabled/>
                        <input id="desc-${i.id}" class="text-sm text-gray-400 bg-transparent outline-none" value="${i.description}" disabled/>
                    </div>
                    </div>

                    <div id="todo-${i.id}" class="flex items-center gap-3 ml-4">
                        <button onclick="enableEdit(${i.id})" class="text-gray-500 hover:text-yellow-400">
                            <i class="fas fa-pencil-alt"></i>
                        </button>
                        <button onclick="saveEdit(${i.id})" class="text-gray-500 hover:text-green-400">
                            <i class="fas fa-save"></i>
                        </button>
                        <button onclick="deleteTodo(${i.id})" class="text-gray-500 hover:text-red-500">
                            <i class="fas fa-trash-alt"></i>
                        </button>
                    </div>
                </div>
            `;
        }
    });

function enableEdit(id) {
    document.getElementById(`title-${id}`).disabled = false;
    document.getElementById(`desc-${id}`).disabled = false;
    document.getElementById(`title-${id}`).focus();
}

// 💾 Save the updated todo
function saveEdit(id) {
    const title = document.getElementById(`title-${id}`).value;
    const description = document.getElementById(`desc-${id}`).value;

    fetch(`http://127.0.0.1:8000/apiedittodo/${id}/`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ title, description })
    })
    .then(response => {
        if (response.ok) {
            location.reload();
        } else {
            alert("Failed to save.");
        }
    });
}

function deleteTodo(id) {
    fetch(`http://127.0.0.1:8000/apideletetodo/${id}/`, {
        method: 'POST'
    })
    .then(response => {
        if (response.ok) {
            document.getElementById(`todo-${id}`).remove();
        } else {
            alert("Failed to delete.");
        }
    });
}