import React, { useState } from 'react';
import { Rating, TextField } from '@mui/material';
import { FaStar, FaRegStar } from 'react-icons/fa';
import { RiFolderUserLine } from 'react-icons/ri';
import { MdEdit } from 'react-icons/md';
import Image from 'next/image';
import Link from 'next/link';

function DoctorInfo({
	name,
	descr,
	about,
	specialization,
	phone,
	date,
	email,
	rate,
}) {
	const [showForm, setShowForm] = useState(false);
	const [emailVal, setEmailVal] = useState(email);
	const [aboutVal, setAboutVal] = useState(about);
	const [dateVal, setDateVal] = useState(date);
	const [specializationVal, setSpecializationVal] = useState(specialization);
	const [phoneVal, setPhoneVal] = useState(phone);

	return (
		<div
			className='p-3 bg-[#fff] rounded-3xl drop-shadow-lg w-[65vw] h-[45vh]
         py-7 px-10 flex flex-col justify-between'
		>
			<div className='flex flex-row'>
				<Image
					className='h-[15vh] w-[8vw] object-cover rounded-[20px]'
					src='/profile.jpg'
					width={160}
					height={160}
					alt='your photo'
				/>
				<div className='ml-7 flex-grow'>
					<div className='flex flex-row justify-between w-full'>
						<div>
							<div className='text-[23px] font-medium text-primary'>{name}</div>
							<div className='text-[12px] text-dark-gray'>{descr}</div>
						</div>
						{showForm ? (
							<></>
						) : (
							<button
								className='text-[32px] text-primary items-center'
								onClick={() => setShowForm((prevCheck) => !prevCheck)}
							>
								<MdEdit className='border border-primary p-1 rounded-lg' />
							</button>
						)}
					</div>

					{showForm ? (
						<form className='h-[220px] flex flex-col py-10'>
							<div className='flex justify-between'>
								<div>
									<div className='text-dark-gray text-[19px] pb-3'>About</div>
									<div className='text-[14px] w-[15vw] pb-[51px]'>
										<TextField
											multiline
											rows={6}
											maxRows={7}
											value={aboutVal}
											onChange={(e) => setAboutVal(e.target.value)}
										/>
									</div>
								</div>
								<div>
									<div>
										<div className='text-dark-gray text-[19px] pb-3'>
											Specialization
										</div>
										<div className='text-[14px] w-[15vw] pb-[51px]'>
											<TextField
												id='outlined-basic'
												size='small'
												value={specializationVal}
												onChange={(e) => setSpecializationVal(e.target.value)}
												variant='outlined'
											/>
										</div>
									</div>
									<div>
										<div className='text-dark-gray text-[19px] pb-3'>
											Phone number
										</div>
										<div className='text-[14px] w-[15vw]'>
											<TextField
												id='outlined-basic'
												size='small'
												value={phoneVal}
												onChange={(e) => setPhoneVal(e.target.value)}
												variant='outlined'
											/>
										</div>
									</div>
								</div>
								<div>
									<div>
										<div className='text-dark-gray text-[19px] pb-3'>
											Date Of Birth
										</div>
										<div className='text-[14px] w-[15vw] pb-[51px]'>
											<TextField
												id='outlined-basic'
												size='small'
												value={dateVal}
												onChange={(e) => setDateVal(e.target.value)}
												variant='outlined'
											/>
										</div>
									</div>
									<div>
										<div className='text-dark-gray text-[19px] pb-3'>Email</div>
										<div className='text-[14px] w-[15vw] pb-[45px]'>
											<TextField
												id='outlined-basic'
												size='small'
												value={emailVal}
												onChange={(e) => setEmailVal(e.target.value)}
												variant='outlined'
											/>
										</div>
									</div>
								</div>
							</div>
							<div className='flex justify-end'>
								<button
									type='submit'
									onClick={() => setShowForm((prevCheck) => !prevCheck)}
									className='bg-primary hover:bg-primary-dark text-white font-bold py-4 px-[70px] rounded-lg'
								>
									Submit
								</button>
							</div>
						</form>
					) : (
						<div className='h-[220px] flex justify-between py-10'>
							<div>
								<div className='text-dark-gray text-[19px] pb-3'>About</div>
								<div className='text-[14px] w-[15vw] pb-[70px]'>{aboutVal}</div>
							</div>
							<div>
								<div>
									<div className='text-dark-gray text-[19px] pb-3'>
										Specialization
									</div>
									<div className='text-[14px] w-[15vw] pb-[70px]'>
										{specializationVal}
									</div>
								</div>
								<div>
									<div className='text-dark-gray text-[19px] pb-3'>
										Phone number
									</div>
									<div className='text-[14px] w-[15vw] pb-[70px]'>
										{phoneVal}
									</div>
								</div>
							</div>
							<div>
								<div>
									<div className='text-dark-gray text-[19px] pb-3'>
										Date Of Birth
									</div>
									<div className='text-[14px] w-[15vw] pb-[70px]'>
										{dateVal}
									</div>
								</div>
								<div>
									<div className='text-dark-gray text-[19px] pb-3'>Email</div>
									<div className='text-[14px] w-[15vw] pb-[70px]'>
										{emailVal}
									</div>
								</div>
							</div>
						</div>
					)}
				</div>
			</div>

			{showForm ? (
				<> </>
			) : (
				<div className='flex flex-row justify-between'>
					<div className='stars'>
						<div className='text-dark-gray text-[19px]'>Rate</div>
						<div>
							<Rating
								defaultValue={rate}
								readOnly
								icon={<FaStar fontSize='20px' />}
								emptyIcon={<FaRegStar fontSize='20px' />}
							/>
						</div>
					</div>
					<div className='flex flex-row items-center'>
						<div className='text-[22px] text-primary pr-[5px]'>
							<RiFolderUserLine />
						</div>
						<Link href='/User/UserListPage'>
							<div className='text-primary'>CURRENT PATIENTS</div>
						</Link>
					</div>
				</div>
			)}
		</div>
	);
}

export default DoctorInfo;
