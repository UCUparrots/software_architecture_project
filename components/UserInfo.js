import { useState, useContext } from 'react';
import { TextField } from '@mui/material';
import { RiFolderUserLine } from 'react-icons/ri';
import { MdEdit } from 'react-icons/md';
import Image from 'next/image';
import { MyContext } from '@/AppStateProvider';
import Link from 'next/link';
import { Alert, AlertTitle } from '@mui/material';
import axios from 'axios';

function UserInfo({ id, name, phone, date, email }) {
	const { isDoctor, userId } = useContext(MyContext);
	const [showForm, setShowForm] = useState(false);
	const [showWarning, setShowWarning] = useState(false);

	const [emailVal, setEmailVal] = useState(email);
	const [dateVal, setDateVal] = useState(date);
	const [phoneVal, setPhoneVal] = useState(phone);

	const handleShowWarning = () => {
		setShowWarning(true);
	};

	const handleCloseWarning = () => {
		setShowWarning(false);
	};

	const inputStyle = {
		color: '#8E8F94',
		borderRadius: '10px',
	};

	const handleChangeData = async (event) => {
		event.preventDefault();
		const url = '/loginS/update_info';
		if (emailVal.length == 0 || dateVal.length == 0 || phoneVal.length == 0) {
			handleShowWarning();
		} else {
			const data = {
				user_id: id,
				email: emailVal,
				phone: phoneVal,
				birthdate: dateVal,
			};
			const headers = {
				'Content-Type': 'application/json',
			};

			try {
				const response = await axios.post(url, data, { headers });
				console.log(response.data);
			} catch (error) {
				console.error(error);
			}
			setShowForm(!showForm);
		}
	};

	return (
		<div
			className='bg-[#fff] rounded-3xl drop-shadow-lg w-[40vw] h-[50vh]
         py-7 px-10 flex flex-col justify-between'
		>
			<div className='flex flex-row'>
				<Image
					className='h-[160px] w-[160px] object-cover rounded-[20px]'
					src='/profile.jpg'
					width={160}
					height={160}
					alt='your photo'
				/>
				<div className='flex justify-between flex-grow'>
					<div className='text-[23px] font-medium text-primary px-5'>
						{name}
					</div>
					<div>
						{showForm || isDoctor ? (
							<></>
						) : (
							<button
								className='text-[32px] text-primary'
								onClick={() => setShowForm((prevCheck) => !prevCheck)}
							>
								<MdEdit className='border border-primary p-1 rounded-lg' />
							</button>
						)}
					</div>
					{showWarning && (
						<Alert severity='error' onClose={handleCloseWarning}>
							<AlertTitle>Error</AlertTitle>
							Input all fields
						</Alert>
					)}
				</div>
			</div>

			<div>
				{showForm ? (
					<form
						className='h-[220px] flex flex-col pb-10'
						onSubmit={handleChangeData}
					>
						<div className='flex justify-between'>
							<div>
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
								<div>
									<div className='text-dark-gray text-[19px] pb-3'>Email</div>
									<div className='text-[14px] w-[15vw] pb-3'>
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
							</div>
						</div>
						<div className='flex justify-end'>
							<button
								type='submit'
								className='bg-primary hover:bg-primary-dark text-white font-bold py-2 px-[20px] rounded-lg'
							>
								Submit
							</button>
						</div>
					</form>
				) : (
					<div className='h-[220px] flex justify-between pt-3'>
						{/* <div>
								<div className='text-dark-gray text-[19px] pb-3'>About</div>
								<div className='text-[14px] w-[15vw] pb-[70px]'>{aboutVal}</div>
							</div> */}
						<div>
							<div>
								<div className='text-dark-gray text-[19px] pb-3'>
									Phone number
								</div>
								<div className='text-[14px] w-[15vw] pb-[70px]'>{phoneVal}</div>
							</div>
							<div>
								<div className='text-dark-gray text-[19px] pb-3'>Email</div>
								<div className='text-[14px] w-[15vw] pb-[70px]'>{emailVal}</div>
							</div>
						</div>
						<div>
							<div>
								<div className='text-dark-gray text-[19px] pb-3'>
									Date Of Birth
								</div>
								<div className='text-[14px] w-[15vw] pb-[70px]'>{dateVal}</div>
							</div>
						</div>
					</div>
				)}
			</div>
			<div>
				{showForm ? (
					<> </>
				) : (
					<Link
						className='flex flex-row justify-end mr-8'
						href={{
							pathname: '/HealthCardPage',
							query: { id: id }, // the data
						}}
					>
						<div className='text-[22px] text-primary pr-[5px]'>
							<RiFolderUserLine />
						</div>
						<div className='text-primary'>{isDoctor ? 'CARD' : 'MY CARD'}</div>
					</Link>
				)}
			</div>
		</div>
	);
}

export default UserInfo;
