function loadEvents(eventType) {
    const baseUrl = window.location.origin; 
    fetch(`${baseUrl}/stage/get-events/${eventType}/`)
        .then(response => response.json())
        .then(data => {
            const eventsContainer = document.getElementById('events-container');
            eventsContainer.innerHTML = '';
            data.events.forEach(event => {
                const eventDiv = document.createElement('div');
                eventDiv.classList.add('register');
                eventDiv.innerHTML = `
                    <label class="title">
                        <h2>${event.title}</h2>
                    </label>
                    <div class="register-btn">
                        <div class="regis">
                            <i class='bx bx-check'></i>
                            <a href="#" onclick="showEventDetail(${event.id})">${event.is_registered ? 'Unregister' : 'Register'}</a>
                        </div>
                        <div class="deets">
                            <i class='bx bx-windows'></i>
                            <a href="#" onclick="showEventDetail(${event.id})">See Details</a>
                        </div>
                    </div>
                `;
                eventsContainer.appendChild(eventDiv);
            });
        })
        .catch(error => console.error('Error loading events:', error));
}

function showEventDetail(eventId) {
    const baseUrl = window.location.origin;; // Adjust baseUrl if necessary
    fetch(`${baseUrl}/stage/get-event/${eventId}/`)
        .then(response => response.json())
        .then(event => {
            document.getElementById('event-title').innerText = event.title;
            document.getElementById('event-description').innerText = event.description;
            document.getElementById('event-location').innerText = event.location;
            document.getElementById('event-times').innerText = `${event.start_time} - ${event.end_time}`;

            const registerBtn = document.getElementById('register-btn');
            registerBtn.innerText = event.is_registered ? 'Unregister' : 'Register';
            registerBtn.onclick = () => registerUnregister(event.id, event.is_registered);

            document.getElementById('events-container').style.display = 'none';
            document.getElementById('event-detail').style.display = 'block';
        })
        .catch(error => console.error('Error loading event detail:', error));
}

function registerUnregister(eventId, isRegistered) {
    const baseUrl = window.location.origin; // Adjust baseUrl if necessary
    const url = isRegistered ? `${baseUrl}/stage/unregister/${eventId}/` : `${baseUrl}/stage/register/${eventId}/`;
    fetch(url, {
        method: 'POST',
        headers: {
            'X-CSRFToken': '{{ csrf_token }}'
        }
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            loadEvents(document.querySelector('a.active').dataset.eventType); // Reload the events list
        } else {
            alert('Error registering/unregistering');
        }
    })
    .catch(error => console.error('Error registering/unregistering:', error));
}

document.addEventListener('DOMContentLoaded', () => {
    console.log("Document loaded, loading upcoming events by default");
    loadEvents('upcoming'); // Load upcoming events by default
});
