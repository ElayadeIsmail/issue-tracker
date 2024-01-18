import { A, RouteSectionProps } from '@solidjs/router';
import { BugIcon } from '~/components/icons';
import { Button } from '~/components/ui/Button';

const BaseLayout = (props: RouteSectionProps) => {
	return (
		<>
			<header class='container flex items-center justify-between h-16 border-b'>
				<A href='/'>
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
			<main class='h-[calc(100vh-64px)] max-w-5xl container flex justify-center'>
				{props.children}
			</main>
		</>
	);
};

export default BaseLayout;
