import { createContext, createResource } from 'solid-js';
import { JSX } from 'solid-js/h/jsx-runtime';
import { createStore } from 'solid-js/store';

export const AuthContext = createContext(null);

interface StoreProps {
	status: 'idle' | 'signIn' | 'signOut';
	token: string | null;
}

export function CounterProvider(props: { children: JSX.Element }) {
	const [state, setState] = createStore<StoreProps>({
		token: null,
		status: 'idle',
	});
	const actions = {
		signIn: (token: string) => {
			setState('token', token);
			setState('status', 'signIn');
		},
		signOut: () => {
			setState('token', null);
			setState('status', 'signOut');
		},
		hydrate: () => {
			const token = localStorage.getItem('jwt');
			if (token) {
				actions.signIn(token);
			} else {
				setState('token', null);
				setState('status', 'signOut');
			}
		},
	};
	const [currentUser, { mutate }] = createResource(state.status, () => {
		return null;
	});

	return (
		<CounterContext.Provider value={counter}>
			{props.children}
		</CounterContext.Provider>
	);
}
