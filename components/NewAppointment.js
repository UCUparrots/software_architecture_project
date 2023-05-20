import Calendar from 'react-calendar';
import 'react-calendar/dist/Calendar.css';
import styled from 'styled-components';
import Select from 'react-select';
import { clsx } from 'clsx';
import { useState } from 'react';
import { BsCheckCircle } from 'react-icons/bs';

function NewAppointment() {
	const [pickedDate, onPickedDate] = useState(new Date());
	const [selectedDoctor, setSelectedDoctor] = useState(null);
	const [selectedService, setSelectedService] = useState(null);
	const [appAdded, setAppAdded] = useState(false);

	const optionsD = [
		{ value: '1', label: 'dr. Sherlock' },
		{ value: '2', label: 'dr. Strange' },
	];

	const optionsS = [
		{ value: '1', label: 'Examination' },
		{ value: '2', label: 'Vacinacion' },
	];

	function submitAppointment() {
		if (selectedDoctor != null && selectedService != null) {
			const response = {
				doctor: selectedDoctor.value,
				service: selectedService.value,
				date: pickedDate,
			};
			setAppAdded(true);
		} else {
			alert('Input all fields');
		}
	}

	return (
		<>
			{appAdded ? (
				<div
					className='bg-[#fff] rounded-3xl drop-shadow-lg w-[55vw] h-[65vh]
         py-7 px-10 flex justify-center items-center'
				>
					<div className='border border-[#1F7711] p-3 rounded-md flex items-center'>
						<div className='text-[#1F7711] text-3xl pr-3'>
							<BsCheckCircle />
						</div>
						<div className='text-[#1F7711]'>
							Your Appointment Was Successfuly Added
						</div>
					</div>
				</div>
			) : (
				<div
					className='bg-[#fff] rounded-3xl drop-shadow-lg w-[55vw] h-[65vh]
         py-7 px-10 flex flex-col justify-between'
				>
					<div className='flex justify-between mt-[7vw]'>
						<div>
							<Select
								options={optionsD}
								classNames={{
									control: ({ isFocused }) =>
										clsx(
											'w-[18vw] h-[5vh] rounded-xl mb-11',
											isFocused ? 'border-gray' : 'border-primary'
										),
								}}
								value={selectedDoctor}
								onChange={(selectedDoctor) => setSelectedDoctor(selectedDoctor)}
								placeholder='Doctor'
							/>
							<Select
								options={optionsS}
								classNames={{
									control: ({ isFocused }) =>
										clsx(
											'w-[18vw] h-[5vh] rounded-xl mb-11 border-primary',
											isFocused ? 'border-primary' : 'border-gray'
										),
								}}
								value={selectedService}
								onChange={(selectedService) =>
									setSelectedService(selectedService)
								}
								placeholder='Service'
							/>
						</div>
						<div>
							<div className='p-2 bg-primary rounded-lg mb-5'>
								<Calendar
									locale='en'
									onChange={onPickedDate}
									value={pickedDate}
									tileDisabled={({ date, view }) =>
										view === 'month' && // Block day tiles only
										getTakenDates().some(
											(disabledDate) =>
												date.getFullYear() === disabledDate.getFullYear() &&
												date.getMonth() === disabledDate.getMonth() &&
												date.getDate() === disabledDate.getDate()
										)
									}
									className={['calendar']}
								/>
							</div>
							<div className='mb-1 ml-3'>Take time slot</div>
							<Select
								classNames={{
									control: ({ isFocused }) =>
										clsx(
											'w-[18vw] h-[5vh] rounded-xl mb-11',
											isFocused ? 'border-gray' : 'border-primary'
										),
								}}
							/>
						</div>
					</div>
					<div className='flex justify-end'>
						<button
							className='bg-primary text-white rounded-md px-8 py-3'
							onClick={submitAppointment}
						>
							CONFIRM
						</button>
					</div>
				</div>
			)}
		</>
	);
}

function getTakenDates() {
	const disabledDates = [
		new Date(2023, 4, 3),
		new Date(2023, 4, 4),
		new Date(2023, 4, 8),
	];
	return disabledDates;
}

export default NewAppointment;
