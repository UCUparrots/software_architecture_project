import DoctorInfo from '@/components/DoctorInfo';
import Layout from '@/components/Layout';

function DoctorInfoPage({ info }) {
	info = JSON.parse(info);

	return (
		<Layout>
			<div>
				<h1 className='text-[46px] font-medium m-[12px] text-primary-dark'>
					Personal Info
				</h1>
				<DoctorInfo
					name={info.firstname + ' ' + info.lastname}
					descr={info.doctor_phd}
					specialization={info.doctor_specialization}
					phone={info.phone}
					date={info.birthdate}
					email={info.email}
					rate={4}
				/>
			</div>
		</Layout>
	);
}

export default DoctorInfoPage;
