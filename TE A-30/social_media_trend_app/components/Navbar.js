import React from 'react'
import Image from 'next/image'

const Navbar = () => {
  return (
    <div className='bg-purple-900 h-[30%] w-[100%] text-white '>
        <div className='flex gap-3 p-3 pl-11'>

        <Image
        src="/image/main_image.png"
        alt="icon"
        width={37}
        height={37}
        />
        <div className='text-xl font-bold'>
            SocialSphere
        </div>
      
      
        </div>
    </div>
  )
}

export default Navbar
