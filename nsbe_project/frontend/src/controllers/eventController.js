import axios from 'axios';
import Cookies from 'js-cookie';

const API_URL = 'http://127.0.0.1:8000/stage/events';

export const handleRegister = async (eventId) => {
    const csrfToken = Cookies.get('csrftoken');
    if (!csrfToken) {
        console.error("CSRF token is not available. ", csrfToken);
    }

    const allCookies = Cookies.get();
    console.log('Available cookies:', allCookies);

    try {
        await axios.post(
            `${API_URL}/${eventId}/register/`,
            {},
            {
                headers: {
                    'X-CSRFToken': csrfToken,
                },
                withCredentials: true
            }
        );
        return { success: true };
    } catch (error) {
        console.error('Failed to register:', error);
        return { success: false, error };
    }
};

export const handleUnregister = async (eventId) => {
    const csrfToken = Cookies.get('csrftoken');
    console.log("CSRF Token: ", csrfToken);
    try {
        await axios.post(
            `${API_URL}/${eventId}/unregister/`,
            {},
            {
                headers: {
                    'X-CSRFToken': csrfToken
                },
                withCredentials: true
            }
        );
        return { success: true };
    } catch (error) {
        console.error('Failed to unregister:', error);
        return { success: false, error };
    }
};
