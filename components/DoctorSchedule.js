import React from 'react';
import FullCalendar from '@fullcalendar/react'; // must go before plugins
import dayGridPlugin from '@fullcalendar/daygrid';
import timeGridPlugin from '@fullcalendar/timegrid';

function DoctorSchedule() {
	return (
		<div className='flex bg-[#fff] w-[90vw] rounded-2xl'>
			<div className='bg-primary-light w-[15vw] rounded-l-2xl'></div>
			<div>
				<FullCalendar
					plugins={[dayGridPlugin, timeGridPlugin]}
					initialView='dayGridMonth'
					headerToolbar={{
						left: 'prev,next',
						center: 'title',
						right: 'dayGridMonth,timeGridWeek,timeGridDay',
					}}
					events={[
						{
							title: 'Event 1',
							start: '2023-05-01T09:00:00',
							end: '2023-05-01T10:30:00',
						},
						{
							title: 'Event 2',
							start: '2023-05-03T14:00:00',
							end: '2023-05-03T16:00:00',
						},
					]}
				/>
			</div>
		</div>
	);
}

export default DoctorSchedule;
