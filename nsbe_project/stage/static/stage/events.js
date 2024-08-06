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
                        <div class="deets">
                            <i class='bx bx-windows'></i>
                            <a href="#" onclick="showEventDetail(${event.id})">See Details</a>
                        </div>
                        ${eventType === 'upcoming' ? `
                        <div class="regis">
                            <i class='bx bx-check'></i>
                            <a href="#" onclick="registerUnregister(${event.id}, ${event.is_member_registered}, false)">${event.is_member_registered ? 'Unregister' : 'Register'}</a>
                        </div>` : ''}
                    </div>
                `;
                eventsContainer.appendChild(eventDiv);
                document.getElementById('event-detail').style.display = 'none';
                document.getElementById('events-container').style.display = 'flex';
            });
        })
        .catch(error => console.error('Error loading events:', error));
}

function showEventDetail(eventId) {
    const baseUrl = window.location.origin; // Adjust baseUrl if necessary
    fetch(`${baseUrl}/stage/get-event/${eventId}/`)
        .then(response => response.json())
        .then(event => {
            document.getElementById('event-title').innerText = event.title;
            document.getElementById('event-description').innerText = event.description;
            document.getElementById('event-location').innerText = event.location;
            document.getElementById('event-times').innerText = `${event.start_time} - ${event.end_time}`;

            const registerBtn = document.getElementById('register-btn');
            var now = new Date();
            const startTime = new Date(event.start_time);
            if (now < startTime) {
                registerBtn.style.display = 'block';
                registerBtn.innerText = event.is_member_registered ? "Unregister" : "Register";
                registerBtn.onclick = () => registerUnregister(event.id, event.is_member_registered);
            } else {
                registerBtn.style.display = 'none';
            }
            registerBtn.onclick = () => registerUnregister(event.id, event.is_member_registered, true);

            document.getElementById('events-container').style.display = 'none';
            document.getElementById('event-detail').style.display = 'block';
        })
        .catch(error => console.error('Error loading event detail:', error));
}

function getCookie(name) {
    const value = `; ${document.cookie}`;
    const parts = value.split(`; ${name}=`);
    if (parts.length === 2) return parts.pop().split(';').shift();
}

const csrftoken = getCookie('csrftoken');

function registerUnregister(eventId, isRegistered, onDetailPage) {
    const baseUrl = window.location.origin; // Adjust baseUrl if necessary
    const url = isRegistered ? `${baseUrl}/stage/unregister/${eventId}/` : `${baseUrl}/stage/register/${eventId}/`;
    fetch(url, {
        method: 'POST',
        headers: {
            'X-CSRFToken': csrftoken
        }
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            if (onDetailPage) {
                showEventDetail(eventId); // Remain on the event detail page
            } else {
                loadEvents('upcoming'); // Reload the list of upcoming events
            }
            console.log(isRegistered ? "Unregistered successfully!" : "Registered successfully!");
        } else {
            console.log('Error registering/unregistering');
        }
    })
    .catch(error => console.error('Error registering/unregistering:', error));
}

document.addEventListener('DOMContentLoaded', () => {
    loadEvents('upcoming'); // Load upcoming events by default
});
