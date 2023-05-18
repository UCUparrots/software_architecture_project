import Appointment from '@/components/Appointment';
import Layout from '@/components/Layout';
import { useRouter } from 'next/router';

function AppointmentPage() {
	let date = new Date();
	date = date.toLocaleDateString('en-US');

	const router = useRouter();
	const { id } = router.query;

	return (
		<Layout>
			<div>
				<h1 className='text-[46px] font-medium m-[12px] text-primary-dark'>
					Health Card
				</h1>
				<Appointment
					clName='Ilya Konsty'
					dcName='Holmes'
					date={date}
					service='Doctors appointment'
					diagnosis='Pneumonia'
					notes='The patient has a new type of illness'
					medicine='Somebody mixed my medicine'
					birth={date}
					residence='Kyiv'
				/>
			</div>
		</Layout>
	);
}

export default AppointmentPage;
