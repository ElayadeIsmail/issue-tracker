/* @refresh reload */
import { Router } from '@solidjs/router'; // 👈 Import the router
import { render } from 'solid-js/web';

import App from './App';
import './styles/app.css';
import './styles/font.css';

const root = document.getElementById('root');

render(
	() => (
		<Router>
			<App />
		</Router>
	),
	root!
);
