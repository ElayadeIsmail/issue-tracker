import { defineConfig } from 'vite';
import solid from 'vite-plugin-solid';

export default defineConfig({
	resolve: {
		alias: [{ find: '~', replacement: '/src' }],
	},
	plugins: [solid()],
});
