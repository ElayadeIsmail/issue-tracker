import { Expandable } from '../Expandable';

type InputErrorProps = {
	name: string;
	error?: string;
};

/**
 * Input error that tells the user what to do to fix the problem.
 */
export function InputError(props: InputErrorProps) {
	return (
		<Expandable expanded={!!props.error}>
			<span
				class='pt-4 text-sm text-red-500 dark:text-red-400 '
				id={`${props.name}-error`}>
				{props.error}
			</span>
		</Expandable>
	);
}
