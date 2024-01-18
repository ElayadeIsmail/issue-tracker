import { action, useAction } from '@solidjs/router';
import { TextInput } from '../form/InputForm';
import { Button } from '../ui/Button';

const loginAction = action(async (username: string, password: string) => {},
'login');

const LoginForm = () => {
	const submit = useAction(loginAction);
	return (
		<div class='mx-auto space-y-4 w-full max-w-md px-8 mt-8'>
			<form class='space-y-4' method='post'>
				<TextInput
					placeholder='username'
					name='username'
					label='Username'
					type='text'
				/>
				<TextInput
					placeholder='********'
					label='Password'
					name='password'
					type='password'
				/>
				<Button size='full'>Submit</Button>
			</form>
			{/* Form Goes Here */}
			<div class='flex items-center justify-center gap-2 '>
				<span class='text-muted-foreground'>New here?</span>
				<a href='/register'>Create an account</a>
			</div>
		</div>
	);
};

export default LoginForm;
