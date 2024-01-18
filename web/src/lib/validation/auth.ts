import { Input, minLength, object, regex, string } from 'valibot';

export const LoginSchema = object({
	username: string([
		minLength(1, 'Please enter your username.'),
		minLength(3, 'Your username must have 3 characters or more.'),
		regex(
			/^[a-zA-Z0-9-]+$/,
			'Invalid username format. Use only letters, numbers, and dashes.'
		),
	]),
	password: string([
		minLength(1, 'Please enter your password.'),
		minLength(8, 'Your password must have 8 characters or more.'),
	]),
});

export type LoginForm = Input<typeof LoginSchema>;
