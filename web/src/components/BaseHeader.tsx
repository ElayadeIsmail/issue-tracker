import { A } from '@solidjs/router';
import { BugIcon } from './icons';
import { Button } from './ui/Button';

export function BaseHeader() {
	return (
		<header class='container flex items-center justify-between h-16 border-b'>
			<A  href='/'>
				<BugIcon />
			</A>
			<nav class='space-x-2'>
				<A href='/login'>
					<Button>Login</Button>
				</A>
				<A href='/register'>
					<Button variant='secondary'>Register</Button>
				</A>
			</nav>
		</header>
	);
}
