import { useState, useContext } from 'react';
import { MdEdit } from 'react-icons/md';
import { RiHealthBookLine, RiFolderUserLine } from 'react-icons/ri';
import { BsBook } from 'react-icons/bs';
import { CgPill } from 'react-icons/cg';
import Link from 'next/link';
import 'react-calendar/dist/Calendar.css';
import { MyContext } from '@/AppStateProvider';
import { TextField } from '@mui/material';
import { VscGroupByRefType } from 'react-icons/vsc';
import DiagnosisHistory from './DiagnosisHistory';
import { LocalizationProvider } from '@mui/x-date-pickers';
import { AdapterDayjs } from '@mui/x-date-pickers/AdapterDayjs';
import { DatePicker } from '@mui/x-date-pickers/DatePicker';
import dayjs, { Dayjs } from 'dayjs';

function HealthCard({ data }) {
	const [showForm, setShowForm] = useState(false);
	const [clNameVal, setClNameVal] = useState(data.clName);
	const [diagnosisVal, setDiagnosisVal] = useState(data.diagnosis);
	const [medicineVal, setMedicineVal] = useState(data.medicine);
	const [notesVal, setNotesVal] = useState(data.notes);
	const [sDateVal, setSDateVal] = useState(data.startDate);
	const [rDateVal, setRDateVal] = useState(data.resolvedDate);

	const { isDoctor, isAppointmentOpen, setIsAppointmentOpen } =
		useContext(MyContext);

	const handleSDateChange = (date) => {
		setSDateVal(date.toDate().toLocaleDateString('en-US'));
	};
	const handleRDateChange = (date) => {
		setRDateVal(date.toDate().toLocaleDateString('en-US'));
	};

	return (
		<div
			className={`bg-[#fff] rounded-3xl drop-shadow-lg h-[65vh]
         py-7 px-10 flex flex-col relative transition-all duration-500 ease-in-out ${
						isAppointmentOpen ? 'w-[50vw]' : 'w-[55vw]'
					}`}
		>
			<div className='flex justify-between mb-8'>
				<div
					className='bg-gray rounded-lg w-[15vw] h-[7vh]
         flex justify-around items-center ml-5'
				>
					<div>
						<div className='text-dark-gray text-sm'>Client</div>
						<div className='text-primary text-xl font-medium'>{clNameVal}</div>
					</div>
				</div>
				{!isDoctor || showForm ? (
					<></>
				) : (
					<div>
						<button
							className='text-[32px] text-primary'
							onClick={() => setShowForm((prevCheck) => !prevCheck)}
						>
							<MdEdit className='border border-primary p-1 rounded-lg' />
						</button>
					</div>
				)}
			</div>

			<div className='flex justify-between flex-grow mt-[4vh] ml-[2vw]'>
				<div className='flex flex-col justify-between'>
					{showForm ? (
						<form>
							<ul>
								<li className='mb-5'>
									<div className='flex items-center'>
										<div className='pr-2'>
											<RiHealthBookLine className='text-primary text-lg' />
										</div>
										<div className='text-primary text-lg'>Current state</div>
									</div>
									<TextField
										id='outlined-basic'
										size='small'
										value={diagnosisVal}
										onChange={(e) => setDiagnosisVal(e.target.value)}
										variant='outlined'
									/>
								</li>
								<li className='mb-5'>
									<div className='flex items-center'>
										<div className='pr-2'>
											<BsBook className='text-primary text-lg' />
										</div>
										<div className='text-primary text-lg'>Additional Notes</div>
									</div>
									<TextField
										id='outlined-basic'
										size='small'
										value={notesVal}
										onChange={(e) => setNotesVal(e.target.value)}
										variant='outlined'
									/>
								</li>
								<li className='mb-5'>
									<div className='flex items-center'>
										<div className='pr-2'>
											<CgPill className='text-primary text-lg' />
										</div>
										<div className='text-primary text-lg'>Medicine</div>
									</div>
									<TextField
										id='outlined-basic'
										size='small'
										value={medicineVal}
										onChange={(e) => setMedicineVal(e.target.value)}
										variant='outlined'
									/>
								</li>
							</ul>
							<button
								type='submit'
								onClick={() => setShowForm((prevCheck) => !prevCheck)}
								className='bg-primary hover:bg-primary-dark text-white font-bold py-2 px-[20px] rounded-lg'
							>
								Submit
							</button>
						</form>
					) : (
						<ul>
							<li className='mb-10'>
								<div className='flex items-center'>
									<div className='pr-2'>
										<RiHealthBookLine className='text-primary text-lg' />
									</div>
									<div className='text-primary text-lg'>Current state</div>
								</div>
								<div className='text-sm'>{diagnosisVal}</div>
							</li>
							<li className='mb-10'>
								<div className='flex items-center'>
									<div className='pr-2'>
										<BsBook className='text-primary text-lg' />
									</div>
									<div className='text-primary text-lg'>Additional Notes</div>
								</div>
								<div className='text-sm'>{notesVal}</div>
							</li>
							<li className='mb-10'>
								<div className='flex items-center'>
									<div className='pr-2'>
										<CgPill className='text-primary text-lg' />
									</div>
									<div className='text-primary text-lg'>Medicine</div>
								</div>
								<div className='text-sm'>{medicineVal}</div>
							</li>
						</ul>
					)}
				</div>
				<div className='flex flex-col'>
					{showForm ? (
						<div className='text-dark-gray  mb-[3vh]'>
							<div className='flex items-center'>
								<div>Start date:</div>
								<LocalizationProvider dateAdapter={AdapterDayjs}>
									<DatePicker
										value={dayjs(sDateVal)}
										onChange={handleSDateChange}
										slotProps={{
											textField: { size: 'small' },
										}}
									/>
								</LocalizationProvider>
							</div>
							<div className='flex items-center'>
								<div>Resolved date:</div>
								<LocalizationProvider dateAdapter={AdapterDayjs}>
									<DatePicker
										value={dayjs(rDateVal)}
										onChange={handleRDateChange}
										slotProps={{
											textField: { size: 'small' },
										}}
									/>
								</LocalizationProvider>
							</div>
						</div>
					) : (
						<div className='text-dark-gray  mb-[6vh]'>
							<div>Start date: {sDateVal}</div>
							<div>Resolved date: {rDateVal === null ? <></> : rDateVal}</div>
						</div>
					)}
					<div>
						<div className='text-xl text-primary'>History of diagnoses</div>
						<DiagnosisHistory />
					</div>
				</div>
			</div>
			<div className='flex justify-between'>
				<div className='flex flex-row items-center'>
					<div className='text-[22px] text-primary pr-[5px]'>
						<RiFolderUserLine />
					</div>
					<Link
						href={{
							pathname: '/UserInfoPage',
							query: { id: data.id },
						}}
					>
						<div className='text-primary text-sm'>CHECK PATIENT</div>
					</Link>
				</div>
				<div className='flex flex-row items-center'>
					<div className='text-[22px] text-primary pr-[5px]'>
						<VscGroupByRefType />
					</div>
					<button
						onClick={() => setIsAppointmentOpen((prevCheck) => !prevCheck)}
					>
						<div className='text-primary text-sm'>APPOINTSMENTS</div>
					</button>
				</div>
			</div>
		</div>
	);
}

export default HealthCard;
