import { useState } from 'react';
import { MdEdit, MdOutlineMedicalServices } from 'react-icons/md';
import { RiHealthBookLine, RiFolderUserLine } from 'react-icons/ri';
import { BsBook } from 'react-icons/bs';
import { CgPill } from 'react-icons/cg';
import Link from 'next/link';
import Calendar from 'react-calendar';
import 'react-calendar/dist/Calendar.css';
import { MyContext } from '@/AppStateProvider';
import { useContext } from 'react';
import { TextField } from '@mui/material';

function Appointment({
	clName,
	dcName,
	date,
	service,
	diagnosis,
	notes,
	medicine,
	birth,
	residence,
}) {
	const [showForm, setShowForm] = useState(false);
	const [clNameVal, setClNameVal] = useState(clName);
	const [dcNameVal, setDcNameVal] = useState(dcName);
	const [serviceVal, setServiceVal] = useState(service);
	const [diagnosisVal, setDiagnosisVal] = useState(diagnosis);
	const [notesVal, setNotesVal] = useState(notes);
	const [medicineVal, setMedicineVal] = useState(medicine);
	const [birthVal, setBirthVal] = useState(birth);
	const [residenceVal, setResidenceVal] = useState(residence);

	const { isDoctor } = useContext(MyContext);

	return (
		<div
			className='bg-[#fff] rounded-3xl drop-shadow-lg w-[55vw] h-[65vh]
         py-7 px-10 flex flex-col'
		>
			<div className='flex justify-between mb-8'>
				<div
					className='bg-gray rounded-lg w-[25vw] h-[7vh]
         flex justify-around items-center ml-5'
				>
					<div>
						<div className='text-dark-gray text-sm'>Client</div>
						<div className='text-primary text-xl font-medium'>{clNameVal}</div>
					</div>
					<div>
						<div className='text-dark-gray text-sm'>Doctor</div>
						<div className='text-primary text-xl font-medium'>{dcNameVal}</div>
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

			<div className='flex justify-between flex-grow'>
				<div className='flex flex-col justify-between'>
					<div>
						{showForm ? (
							<form>
								<ul>
									<li className='mb-5'>
										<div className='flex items-center mb-2'>
											<div className='pr-2'>
												<MdOutlineMedicalServices className='text-primary text-lg' />
											</div>
											<div className='text-primary text-lg'>Service Type</div>
										</div>
										<TextField
											id='outlined-basic'
											size='small'
											value={serviceVal}
											onChange={(e) => setServiceVal(e.target.value)}
											variant='outlined'
										/>
									</li>
									<li className='mb-5'>
										<div className='flex items-center'>
											<div className='pr-2'>
												<RiHealthBookLine className='text-primary text-lg' />
											</div>
											<div className='text-primary text-lg'>Diagnosis</div>
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
											<div className='text-primary text-lg'>
												Additional Notes
											</div>
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
									<div className='flex items-center mb-2'>
										<div className='pr-2'>
											<MdOutlineMedicalServices className='text-primary text-lg' />
										</div>
										<div className='text-primary text-lg'>Service Type</div>
									</div>
									<div className='text-sm'>{serviceVal}</div>
								</li>
								<li className='mb-10'>
									<div className='flex items-center'>
										<div className='pr-2'>
											<RiHealthBookLine className='text-primary text-lg' />
										</div>
										<div className='text-primary text-lg'>Diagnosis</div>
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
					<div className='flex flex-row items-center'>
						<div className='text-[22px] text-primary pr-[5px]'>
							<RiFolderUserLine />
						</div>
						<Link href='/UserInfoPage'>
							<div className='text-primary text-sm'>CHECK PATIENT</div>
						</Link>
					</div>
				</div>
				<div className='flex flex-col justify-between'>
					<div className='pointer-events-none p-2 bg-primary rounded-lg'>
						<Calendar value={date} locale='en' />
					</div>
					<div className='border-2 border-dark-gray p-1 rounded-lg w-full h-[18vh]'>
						<div className='text-xl text-center mb-3 mt-2'>
							Additional Client Info
						</div>
						<div className='mb-4 ml-1'>
							<div className='flex items-center '>
								<div className='text-primary text-lg'>Date of birth</div>
							</div>
							<div className='text-sm'>{birthVal}</div>
						</div>
						<div className='ml-1'>
							<div className='flex items-center'>
								<div className='text-primary text-lg'>Residence</div>
							</div>
							<div className='text-sm'>{residenceVal}</div>
						</div>
					</div>
				</div>
			</div>
		</div>
	);
}

export default Appointment;
