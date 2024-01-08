import { SubmitHandler, createForm, valiForm } from '@modular-forms/solid';
import { A } from '@solidjs/router';
import MySiteTitle from '~/components/SiteTitle';
import { TextInput } from '~/components/form/InputForm';
import { Button } from '~/components/ui/Button';
import { LoginForm, LoginSchema } from '~/lib/validation/auth';

export default function LoginPage() {
	const [loginForm, { Form, Field }] = createForm<LoginForm>({
		validate: valiForm(LoginSchema),
	});

	const handleSubmit: SubmitHandler<LoginForm> = (values) => {
		// Runs on client
		console.log(values);
	};
	return (
		<>
			<MySiteTitle>Login</MySiteTitle>
			<div class='flex min-h-full flex-col justify-center pt-20'>
				<div class='mx-auto w-full max-w-md'>
					<div class='flex flex-col gap-3 text-center'>
						<h1 class='text-h1 text-primary'>Welcome back!</h1>
						<p class='text-body-md text-muted-foreground'>
							Please enter your details.
						</p>
					</div>
					<div class='mx-auto space-y-4 w-full max-w-md px-8 mt-8'>
						<div>{loginForm.response.message}</div>
						<Form class='space-y-4' onSubmit={handleSubmit}>
							<Field name='username'>
								{(field, props) => (
									<TextInput
										{...props}
										{...field}
										placeholder='username'
										label='Username'
										type='text'
									/>
								)}
							</Field>
							<Field name='password'>
								{(field, props) => (
									<TextInput
										{...props}
										{...field}
										placeholder='********'
										label='Password'
										type='password'
									/>
								)}
							</Field>
							<Button disabled={loginForm.submitting} size='full'>
								{loginForm.submitting
									? 'Submitting..'
									: 'Submit'}
							</Button>
						</Form>
						{/* Form Goes Here */}
						<div class='flex items-center justify-center gap-2 '>
							<span class='text-muted-foreground'>New here?</span>
							<A href='/register'>Create an account</A>
						</div>
					</div>
				</div>
			</div>
		</>
	);
}
