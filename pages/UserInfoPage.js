import Layout from '@/components/Layout';
import { useContext, useState, useEffect } from 'react';
import UserInfo from '@/components/UserInfo';
import { MyContext } from '@/AppStateProvider';
import { useRouter } from 'next/router';

function UserInfoPage() {
	const { isDoctor } = useContext(MyContext);
	const [data, setData] = useState(null);

	const router = useRouter();
	const query = router.query;

	let date = new Date();
	date = date.toLocaleDateString('en-US');

	// useEffect(() => {
	// 	// Perform the HTTP GET request
	// 	fetch('https://api.example.com/data')
	// 		.then((response) => response.json())
	// 		.then((data) => {
	// 			setData(data);
	// 			console.log(data);
	// 		})
	// 		.catch((error) => {
	// 			console.error('Error fetching data:', error);
	// 		});
	// }, []);
	useEffect(() => {
		if (query.id == 0) {
			setData({
				id: query.id,
				name: 'Ilya Konsty',
				phone: '(380) 94 254 44 13',
				date: date,
				email: 'IlyaKonsty@gmail.com',
				residence: 'Kalynivka, Kyiv district',
			});
		} else {
			setData({
				id: query.id,
				name: 'Eduard Roller',
				phone: '(380) 94 254 44 13',
				date: date,
				email: 'eduardo@gmail.com',
				residence: 'Lviv, Kyiv district',
			});
		}
	}, []);

	if (data === null) {
		// Render a loading state while waiting for the data
		return <div>Loading...</div>;
	}

	return (
		<Layout>
			<div>
				<h1 className='text-[46px] font-medium m-[12px] text-primary-dark'>
					{isDoctor ? 'User Info' : 'My Info'}
				</h1>
				<UserInfo
					id={data.id}
					name={data.name}
					phone={data.phone}
					date={data.date}
					email={data.email}
					residence={data.residence}
				/>
			</div>
		</Layout>
	);
}

export default UserInfoPage;
