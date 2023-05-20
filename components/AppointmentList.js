import {
	VerticalTimeline,
	VerticalTimelineElement,
} from 'react-vertical-timeline-component';
import 'react-vertical-timeline-component/style.min.css';
import { FaUser } from 'react-icons/fa';
import { useRouter } from 'next/router';

function AppointmentList({ data, height }) {
	const router = useRouter();

	const goToAppointment = (id) => {
		router.push(`/AppointmentPage?id=${id}`);
	};

	return (
		<div className={`ml-5 overflow-y-auto overflow-hidden h-[${height}]`}>
			<VerticalTimeline lineColor='#4A148C' layout='1-column-left'>
				{data.map((appointment) => (
					<VerticalTimelineElement
						key={appointment.id}
						className='vertical-timeline-element--work'
						contentStyle={{
							background: appointment.past ? '#D9D9D9' : '#4A148C',
							color: appointment.past ? '#4A148C' : '#fff',
						}}
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
						<h3 className='vertical-timeline-element-subtitle text-xl'>
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
