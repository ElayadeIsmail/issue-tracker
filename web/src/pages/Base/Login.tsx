import LoginForm from '~/components/auth/LoginForm';

const Login = () => {
	return (
		<div class='w-full pt-24'>
			<div class='flex flex-col gap-3 text-center'>
				<h1 class='text-h1 text-primary'>Welcome back!</h1>
				<p class='text-body-md text-muted-foreground'>
					Please enter your details.
				</p>
			</div>
			<div class='space-y-4 w-full px-8 mt-8'>
				<LoginForm />
			</div>
		</div>
	);
};

export default Login;
