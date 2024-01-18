import clsx from 'clsx';
import { JSX, splitProps } from 'solid-js';
import { Input } from '../ui/Input';
import { Label } from '../ui/Label';
import { InputError } from './InputError';

interface TextInputProps extends JSX.InputHTMLAttributes<HTMLInputElement> {
	error?: string;
	label?: string;
}

/**
 * Text input field that users can type into. Various decorations can be
 * displayed in or around the field to communicate the entry requirements.
 */
export function TextInput(props: TextInputProps) {
	// Split input element props
	const [, inputProps] = splitProps(props, [
		'class',
		'value',
		'label',
		'error',
	]);

	// // Create memoized value
	// const getValue = createMemo<string | number | undefined | string[]>(
	// 	(prevValue) =>
	// 		props.value === undefined
	// 			? ''
	// 			: !Number.isNaN(props.value)
	// 			? props.value
	// 			: prevValue,
	// 	''
	// );

	return (
		<div class={clsx(props.class)}>
			<Label
				name={props.name!}
				children={props.label}
				// required={props.required}
			/>
			<Input
				{...inputProps}
				error={props.error}
				id={props.name}
				aria-invalid={!!props.error}
				aria-errormessage={`${props.name}-error`}
			/>
			<InputError name={props.name!} error={props.error} />
		</div>
	);
}
