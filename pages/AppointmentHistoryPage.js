import AppointmentList from '@/components/AppointmentList';
import Layout from '@/components/Layout';
import { useRouter } from 'next/router';
import { useEffect, useState } from 'react';

function AppointmentHistoryPage() {
	const [dataApp, setDataApp] = useState(null);

	const router = useRouter();
	const { id } = router.query;

	const options = {
		day: '2-digit',
		month: '2-digit',
		year: 'numeric',
		hour: '2-digit',
		minute: '2-digit',
		second: '2-digit',
	};

	useEffect(() => {
		setDataApp([
			{
				id: 0,
				time: new Date('2022-05-14T17:23:00').toLocaleString('en-GB', options),
				drName: 'Faradey',
				diagnosis: 'Super illness',
				notes:
					'Lorem Ipsum is simply dummy text of the printing and typesetting industry',
				past: true,
			},
			{
				id: 1,
				time: new Date('2023-05-18T10:30:00').toLocaleString('en-GB', options),
				drName: 'Alex',
				diagnosis: 'Super illness',
				notes:
					'Lorem Ipsum is simply dummy text of the printing and typesetting industry',
				past: true,
			},
			{
				id: 2,
				time: new Date('2023-05-18T10:35:00').toLocaleString('en-GB', options),
				drName: 'Boldweyn',
				diagnosis: 'Super illness',
				notes:
					'Lorem Ipsum is simply dummy text of the printing and typesetting industry',
				past: false,
			},
			{
				id: 3,
				time: new Date('2023-08-18T10:10:00').toLocaleString('en-GB', options),
				drName: 'Faradey',
				diagnosis: 'He is OKAY',
				notes:
					'Lorem Ipsum is simply dummy text of the printing and typesetting industry',
				past: false,
			},
		]);
	}, []);

	if (dataApp === null) {
		return <div>Loading...</div>;
	}

	return (
		<Layout>
			<div>
				<h1 className='text-[46px] font-medium m-[12px] text-primary-dark'>
					Your Appointments
				</h1>
				<AppointmentList data={dataApp} height='75vh' />
			</div>
		</Layout>
	);
}

export default AppointmentHistoryPage;
