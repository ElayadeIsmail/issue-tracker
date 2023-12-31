import { VariantProps, cva } from 'class-variance-authority';
import { JSX } from 'solid-js';
import { cn } from '~/lib/utils';

const labelVariants = cva(
	'text-sm font-medium leading-none peer-disabled:cursor-not-allowed peer-disabled:opacity-70'
);

interface LabelProps
	extends JSX.LabelHTMLAttributes<HTMLLabelElement>,
		VariantProps<typeof labelVariants> {
	name: string;
}

export function Label({ class: className, ...props }: LabelProps) {
	return <label class={cn(labelVariants(), className)} {...props} />;
}
