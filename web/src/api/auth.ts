import client from './client';

export const getCurrentUser = async (token: string) => {
	try {
		const data = await client.get('/currentuser', {
			headers: {
				Authorization: 'Bearer ' + token,
			},
		});
		console.log(data);
	} catch (error) {
		console.log(error);
	}
};
