import Layout from '@/components/Layout';
import NewAppointment from '@/components/NewAppointment';

function NewAppointmentPage() {
	return (
		<Layout>
			<div>
				<h1 className='text-[46px] font-medium m-[12px] text-primary-dark'>
					Create Appointment
				</h1>
				<NewAppointment />
			</div>
		</Layout>
	);
}

export default NewAppointmentPage;
