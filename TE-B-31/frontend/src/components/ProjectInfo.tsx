import  { useState } from "react";
import { motion } from "motion/react";
import { RxGithubLogo } from "react-icons/rx";
import googleCollabLogo from "../assets/favicon.ico";
import { FaBookOpen } from "react-icons/fa";
import { FaConnectdevelop } from "react-icons/fa6";

function ProjectInfo() {
    const [viewInfo, setViewInfo] = useState<boolean>(false);

    const shadow = `shadow-[0_1px_12px_rgba(255,255,255,0.5),0_4px_6px_rgba(34,42,53,0.04),0_24px_68px_rgba(47,48,55,0.05),0_2px_3px_rgba(0,0,0,0.04)]`;

    return (
        <>
            {!viewInfo && (
                <div className="absolute w-full top-3 right-3 flex  justify-between items-center">
                    <motion.button
                        initial={{
                            opacity: 0,
                        }}
                        animate={{
                            opacity: 1,
                        }}
                        transition={{
                            duration: 1,
                            delay: 1,
                        }}
                        className={`bg-black text-zinc-500  text-[9px] sm:text-[14px] px-7 py-2 rounded-xl mt-4 flex justify-center items-center gap-2 pl-6 italic ml-1`}
                    >
                        <motion.span>
                            <FaConnectdevelop />
                        </motion.span>
                        Design and Develop by Tejas Shinde{" "}
                    </motion.button>

                    <motion.button
                        initial={{
                            opacity: 0,
                        }}
                        animate={{
                            opacity: 1,
                        }}
                        transition={{
                            duration: 1,
                            delay: 1,
                        }}
                        onClick={()=>setViewInfo(true)}
                        className={`bg-black text-zinc-300 text-nowrap border-zinc-300 text-[12px] sm:text-[14px] px-7 py-2 rounded-xl mt-4 flex justify-center items-center gap-2 pl-6 ${shadow} `}
                    >
                        Project Info{" "}
                        <motion.span>
                            <FaBookOpen />
                        </motion.span>
                    </motion.button>
                </div>
            )}
            {viewInfo && (
                <div className="absolute top-3 right-3 flex gap-2 justify-center items-center">
                    <motion.button
                        initial={{
                            opacity: 0,
                        }}
                        animate={{
                            opacity: 1,
                        }}
                        transition={{
                            duration: 1,
                            delay: .2,
                        }}
                        onClick={()=> window.location.href = "https://github.com/CoderCastor/Spam-Mail-Detection-System" }
                        className={`bg-zinc-300 text-black text-[12px] sm:text-[14px] px-7 py-2 rounded-xl mt-4 flex text-nowrap justify-center items-center gap-2 pl-6 ${shadow} `}
                    >
                        Project Codes{" "}

                        <motion.span>
                            <RxGithubLogo />
                        </motion.span>
                    </motion.button>
                    <motion.button
                    onClick={()=>window.location.href = "https://colab.research.google.com/drive/1qmSlV4w7MITGla5F_yOmOi5yX7-KYZII?usp=sharing"}
                        initial={{
                            opacity: 0,
                        }}
                        animate={{
                            opacity: 1,
                        }}
                        transition={{
                            duration: 1,
                            delay: .2,
                        }}
                        className={`bg-zinc-300 text-black text-[8px] sm:text-[14px] px-7 py-2 rounded-xl mt-4 flex justify-center items-center gap-2 pl-6 ${shadow} `}
                    >
                        <motion.span className="">
                            <img
                                src={googleCollabLogo}
                                className="h-4 scale-150"
                                alt=""
                            />
                        </motion.span>
                        Google Collab Notebook{" "}
                    </motion.button>
                </div>
            )}
        </>
    );
}

export default ProjectInfo;
