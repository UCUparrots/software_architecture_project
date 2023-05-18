import {
	VerticalTimeline,
	VerticalTimelineElement,
} from 'react-vertical-timeline-component';
import 'react-vertical-timeline-component/style.min.css';
import { FaUser } from 'react-icons/fa';
import { useRouter } from 'next/router';

function AppointmentList({ data }) {
	const router = useRouter();

	const goToAppointment = (id) => {
		router.push(`/AppointmentPage?id=${id}`);
	};

	return (
		<div className='ml-5 overflow-y-auto overflow-hidden h-[65vh]'>
			<VerticalTimeline lineColor='#4A148C' layout='1-column-left'>
				{data.map((appointment) => (
					<VerticalTimelineElement
						key={appointment.id}
						className='vertical-timeline-element--work'
						contentStyle={{ background: '#4A148C', color: '#fff' }}
						contentArrowStyle={{ borderRight: '7px solid  #4A148C' }}
						date={appointment.time}
						iconStyle={{
							background: '#4A148C',
							borderColor: '#4A148C',
						}}
						icon={<FaUser />}
						onTimelineElementClick={() => goToAppointment(appointment.id)}
						style={{ cursor: 'pointer' }}
					>
						<h3 className='vertical-timeline-element-subtitle text-white text-xl'>
							Dr. {appointment.drName}
						</h3>
						<p>Diagnosis: {appointment.diagnosis}</p>
						<p>Notes: {appointment.notes}</p>
					</VerticalTimelineElement>
				))}
			</VerticalTimeline>
		</div>
	);
}

export default AppointmentList;
