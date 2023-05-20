import FullCalendar from '@fullcalendar/react'; // must go before plugins
import dayGridPlugin from '@fullcalendar/daygrid';
import timeGridPlugin from '@fullcalendar/timegrid';
import interactionPlugin from '@fullcalendar/interaction';
import { useState, useEffect } from 'react';
import moment from 'moment';

function DoctorSchedule() {
	const [selectedDates, setSelectedDates] = useState([]);

	const handleDateClick = (arg) => {
		const clickedDate = arg.dateStr;

		if (selectedDates.includes(clickedDate)) {
			// Unmark the date if it is already selected
			setSelectedDates(selectedDates.filter((date) => date !== clickedDate));
		} else {
			// Mark the date if it is not selected
			setSelectedDates([...selectedDates, clickedDate]);
		}
	};

	const renderDayCellContent = (args) => {
		const dateStr = moment(args.date).format('YYYY-MM-DD');
		const isSelected = selectedDates.includes(dateStr);

		const cellStyles = {
			backgroundColor: isSelected ? 'gray' : 'inherit',
			color: isSelected ? 'white' : 'inherit',
			// Add any additional CSS properties or styles as needed
		};

		return (
			<div className='custom-day-cell' style={cellStyles}>
				{args.dayNumberText}
			</div>
		);
	};

	useEffect(() => {
		console.log(selectedDates);
	}, [selectedDates]);

	return (
		<div className='flex bg-[#fff] w-[90vw] rounded-2xl h-[80vh]'>
			<div className='bg-primary-light w-[15vw] rounded-l-2xl'>
				<div className='mt-10 ml-7 text-2xl text-primary-dark'>All events</div>
			</div>
			<div className='flex items-center justify-center flex-grow'>
				<FullCalendar
					plugins={[dayGridPlugin, timeGridPlugin, interactionPlugin]}
					initialView='dayGridMonth'
					headerToolbar={{
						left: 'prev,next',
						center: 'title',
						right: 'dayGridMonth,timeGridWeek,timeGridDay',
					}}
					dateClick={handleDateClick}
					dayCellContent={renderDayCellContent}
					events={[
						{
							title: 'Event 1',
							start: '2023-05-01T09:00:00',
							end: '2023-05-01T10:30:00',
						},
						{
							title: 'Event 3',
							start: '2023-05-01T10:45:00',
							end: '2023-05-01T11:00:00',
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
