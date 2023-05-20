import { useState } from 'react';
import { TextField } from '@mui/material';
import { LocalizationProvider } from '@mui/x-date-pickers';
import { AdapterDayjs } from '@mui/x-date-pickers/AdapterDayjs';
import { DatePicker } from '@mui/x-date-pickers/DatePicker';
import dayjs, { Dayjs } from 'dayjs';

function Diagnosis({ diagnosis }) {
	const [sD, setSD] = useState(diagnosis.startDate);
	const [rD, setRD] = useState(diagnosis.resolveDate);
	const [d, setD] = useState(diagnosis.diagnosis);
	const [med, setMed] = useState(diagnosis.medicine);

	const [editMode, setEditMode] = useState(false);

	const edit = () => {
		setEditMode(!editMode);
	};

	const handleSChange = (date) => {
		setSD(date.toDate().toLocaleDateString('en-US'));
	};

	const handleRChange = (date) => {
		setRD(date.toDate().toLocaleDateString('en-US'));
	};

	return (
		<li
			className='h-[10vh] border border-dark-gray rounded-lg mb-1
                        flex justify-between bg-white drop-shadow-md p-2 items-center'
			onDoubleClick={edit}
		>
			{editMode ? (
				<>
					<div className='text-dark-gray'>
						<div className='flex'>
							<div>Start date:</div>
							<LocalizationProvider dateAdapter={AdapterDayjs}>
								<DatePicker
									value={dayjs(sD)}
									onChange={handleSChange}
									slotProps={{
										textField: { size: 'small' },
									}}
									sx={{ width: '8vw' }}
								/>
							</LocalizationProvider>
						</div>
						<div className='flex'>
							<div>Resolve date:</div>
							<LocalizationProvider dateAdapter={AdapterDayjs}>
								<DatePicker
									value={dayjs(rD)}
									onChange={handleRChange}
									slotProps={{
										textField: { size: 'small' },
									}}
									sx={{ width: '8vw' }}
								/>
							</LocalizationProvider>
						</div>
					</div>
					<div>
						<div className='mb-5 flex items-center'>
							<div className='text-dark-gray mr-2'>Diagnosis:</div>
							<TextField
								size='small'
								value={d}
								onChange={(e) => setD(e.target.value)}
								variant='standard'
								sx={{ width: '8vw' }}
							/>
						</div>
						<div className='flex'>
							<div className='text-dark-gray mr-2'>Medicine:</div>
							<TextField
								size='small'
								value={med}
								onChange={(e) => setMed(e.target.value)}
								variant='standard'
								sx={{ width: '8vw' }}
							/>
						</div>
					</div>
				</>
			) : (
				<>
					<div className='text-dark-gray'>
						<div className='mb-5'>Start date: {sD}</div>
						<div>Resolved date: {rD}</div>
					</div>
					<div>
						<div className='mb-5 flex'>
							<div className='text-primary mr-2'>Diagnosis:</div>
							{d}
						</div>
						<div className='flex'>
							<div className='text-primary mr-2'>Medicine:</div>
							{med}
						</div>
					</div>
				</>
			)}
		</li>
	);
}

export default Diagnosis;
