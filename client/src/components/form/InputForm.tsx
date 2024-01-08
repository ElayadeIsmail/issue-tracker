import clsx from 'clsx';
import { createMemo, JSX, splitProps } from 'solid-js';
import { Input } from '../ui/Input';
import { Label } from '../ui/Label';
import { InputError } from './InputError';

type TextInputProps = {
	ref: (element: HTMLInputElement) => void;
	type: 'text' | 'email' | 'tel' | 'password' | 'url' | 'number' | 'date';
	name: string;
	value: string | number | undefined;
	onInput: JSX.EventHandler<HTMLInputElement, InputEvent>;
	onChange: JSX.EventHandler<HTMLInputElement, Event>;
	onBlur: JSX.EventHandler<HTMLInputElement, FocusEvent>;
	placeholder?: string;
	required?: boolean;
	class?: string;
	label?: string;
	error?: string;
	padding?: 'none';
};

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
		'padding',
	]);

	// Create memoized value
	const getValue = createMemo<string | number | undefined>(
		(prevValue) =>
			props.value === undefined
				? ''
				: !Number.isNaN(props.value)
				? props.value
				: prevValue,
		''
	);

	return (
		<div class={clsx(props.class)}>
			<Label
				name={props.name}
				children={props.label}
				// required={props.required}
			/>
			<Input
				{...inputProps}
				error={props.error}
				id={props.name}
				value={getValue()}
				aria-invalid={!!props.error}
				aria-errormessage={`${props.name}-error`}
			/>
			<InputError name={props.name} error={props.error} />
		</div>
	);
}
