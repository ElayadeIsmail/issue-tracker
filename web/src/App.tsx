import { Route } from '@solidjs/router';
import Home from '~/pages/Base';
import Login from '~/pages/Base/Login';
import Register from '~/pages/Base/Register';
import BaseLayout from './layout/BaseLayout';

import Dashboard from '~/pages/Dashboard';
import AuthLayout from './layout/AuthLayout';

function App() {
	return (
		<>
			<Route path='/' component={BaseLayout}>
				<Route path='/' component={Home} />
				<Route path='/login' component={Login} />
				<Route path='/register' component={Register} />
			</Route>
			<Route path='/dashboard' component={AuthLayout}>
				<Route path='/' component={Dashboard} />
			</Route>
		</>
	);
}

export default App;
