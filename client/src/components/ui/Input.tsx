import { JSX } from 'solid-js';
import { cn } from '~/lib/utils';

interface InputProps extends JSX.InputHTMLAttributes<HTMLInputElement> {}

export function Input({ type, class: className, ...props }: InputProps) {
	return (
		<input
			type={type}
			class={cn(
				'flex h-10 w-full bg-input rounded-md border border-input px-3 py-2 text-sm file:border-0 file:bg-transparent file:text-sm file:font-medium placeholder:text-muted-foreground focus-visible:outline-none disabled:cursor-not-allowed disabled:opacity-50',
				className
			)}
			{...props}
		/>
	);
}
