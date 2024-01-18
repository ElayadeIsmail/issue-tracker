import { Title } from '@solidjs/meta';
import { JSX } from 'solid-js';

export default function MySiteTitle(props: { children: JSX.Element }) {
	return <Title>{props.children} | Issue Tracker</Title>;
}
