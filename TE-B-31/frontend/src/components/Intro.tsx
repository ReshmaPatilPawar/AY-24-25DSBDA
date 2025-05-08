import { AnimatePresence, motion } from "motion/react";
import { IoOpenOutline } from "react-icons/io5";
import { TextGenerateEffect } from "./ui/text-generate-effect";

function Intro({ setDisplayIntro,displayIntro }: any) {
    const shadow = `shadow-[0_1px_12px_rgba(255,255,255,0.5),0_4px_6px_rgba(34,42,53,0.04),0_24px_68px_rgba(47,48,55,0.05),0_2px_3px_rgba(0,0,0,0.04)]`;
    return (
        
            <>
            <AnimatePresence>
                {displayIntro && <motion.div
            initial={{
                opacity:0,
                scale:0.98,
                filter:"blur(10px)"

            }}
            animate={{
                opacity:1,
                scale:1,
                filter:"blur(0px)"
            }}
            exit={{
                opacity:0,
                scale:0.98,
                filter:"blur(10px)"
            }}
            transition={{
                duration:0.5,
                ease:"easeInOut"
            }} className="flex flex-col items-center absolute">
                <TextGenerateEffect
                    words="DSBDA Project"
                    duration={1}
                    filter={true}
                    className="sm:text-4xl text-2xl text-purple-800"
                />
                <span className="flex gap-2 sm:gap-4">
                    <TextGenerateEffect
                        words="Spam"
                        duration={2}
                        filter={true}
                        className="text-[22px] sm:text-4xl md:text-5xl lg:text-6xl text-red-300"
                    />
                    <TextGenerateEffect
                        words="Mail Detection System"
                        duration={2}
                        filter={true}
                        className="text-[22px] sm:text-4xl md:text-5xl lg:text-6xl text-zinc-200"
                    />
                </span>

                <motion.button
                    onClick={() => setDisplayIntro(false)}

                    

                    initial={{
                        opacity: 0,
                    }}
                    animate={{
                        opacity: 1,
                    }}
                    transition={{
                        duration: 1,
                        delay: 1.5,
                    }}
                    className={`bg-purple-600 text-white text-[12px] sm:text-[14px] px-4 py-2 rounded-xl mt-4 flex justify-center items-center gap-2 pl-6 ${shadow}`}
                >
                    View Project{" "}
                    <motion.span
                        initial={{
                            scale: 1,
                        }}
                        animate={{
                            rotate: 0,
                            scale: 1.2,
                        }}
                        transition={{
                            duration: 2,
                            delay: 1.7,
                            repeat: 100,
                        }}
                        className="rounded-full px-1 py-1"
                    >
                        <IoOpenOutline />
                    </motion.span>
                </motion.button>

                <motion.p
                    initial={{
                        y: 20,
                        opacity: 0,
                        filter: "blur(10px)",
                    }}
                    animate={{
                        y: 0,
                        opacity: 1,
                        filter: "blur(0px)",
                    }}
                    transition={{
                        duration: 1,
                        delay: 1,
                    }}
                    className="text-white text-[10px] sm:text-[12px] italic px-3 py-1 rounded-3xl mt-7"
                >
                    Design and Develop by Tejas Shinde
                </motion.p>
            </motion.div>}
            </AnimatePresence>
            </>
        
    );
}

export default Intro;
