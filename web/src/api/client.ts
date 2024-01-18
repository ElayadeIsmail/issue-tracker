import axios from 'axios';

const client = axios.create({
	baseURL: 'https://127.0.0.1:8000',
});

export default client;
