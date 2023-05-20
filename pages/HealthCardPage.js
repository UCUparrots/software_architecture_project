import HealthCard from '@/components/HealthCard';
import AppointmentList from '@/components/AppointmentList';
import Layout from '@/components/Layout';
import { useEffect, useState, useContext } from 'react';
import { useRouter } from 'next/router';
import { MyContext } from '@/AppStateProvider';

function HealthCardPage() {
	const [data, setData] = useState(null);
	const [dataApp, setDataApp] = useState(null);

	let sd = new Date();
	sd = sd.toLocaleDateString('en-US');

	const router = useRouter();
	const query = router.query;

	const { isAppointmentOpen } = useContext(MyContext);

	const options = {
		day: '2-digit',
		month: '2-digit',
		year: 'numeric',
		hour: '2-digit',
		minute: '2-digit',
		second: '2-digit',
	};

	useEffect(() => {
		setData({
			id: query.id,
			clName: 'Ilya Konsty',
			diagnosis: 'Ill, pneumonia',
			medicine: 'Paracetamol',
			notes: 'He drinks too much',
			startDate: sd,
			resolvedDate: null,
		});

		setDataApp([
			{
				id: 0,
				time: new Date('2022-05-14T17:23:00').toLocaleString('en-GB', options),
				drName: 'Faradey',
				diagnosis: 'Super illness',
				notes:
					'Lorem Ipsum is simply dummy text of the printing and typesetting industry',
			},
			{
				id: 1,
				time: new Date('2023-05-18T10:30:00').toLocaleString('en-GB', options),
				drName: 'Alex',
				diagnosis: 'Super illness',
				notes:
					'Lorem Ipsum is simply dummy text of the printing and typesetting industry',
			},
			{
				id: 2,
				time: new Date('2023-05-18T10:35:00').toLocaleString('en-GB', options),
				drName: 'Boldweyn',
				diagnosis: 'Super illness',
				notes:
					'Lorem Ipsum is simply dummy text of the printing and typesetting industry',
			},
			{
				id: 3,
				time: new Date('2023-08-18T10:10:00').toLocaleString('en-GB', options),
				drName: 'Faradey',
				diagnosis: 'He is OKAY',
				notes:
					'Lorem Ipsum is simply dummy text of the printing and typesetting industry',
			},
		]);
	}, []);

	if (data === null || dataApp === null) {
		return <div>Loading...</div>;
	}

	return (
		<Layout>
			<h1 className='text-[46px] font-medium m-[12px] text-primary-dark'>
				Health Card
			</h1>
			<div className='flex'>
				<HealthCard data={data} />
				{isAppointmentOpen ? (
					<AppointmentList data={dataApp} height='65vh' />
				) : (
					<></>
				)}
			</div>
		</Layout>
	);
}

export default HealthCardPage;
