import { useState } from "react";
import { motion } from "motion/react";
import { BiAnalyse } from "react-icons/bi";
import { MdEmojiObjects } from "react-icons/md";
import { MdOutlineClearAll } from "react-icons/md";
import { TypewriterEffect } from "./ui/typewriter-effect";
import axios from "axios";
import { RxCross2 } from "react-icons/rx";


function MainSection() {
    const [isAnalyzing, setIsAnalyzing] = useState<boolean>(false);
    const [input, setInput] = useState<string>("");
    const [spamEmail, setSpamEmail] = useState<number>(0);

    const emailSamples = [
        {
          message: "Congratulations! You've won an all-expense-paid luxury cruise to the Bahamas. This exclusive offer is valid for a limited time only. To claim your tickets, please click the link below and complete the short registration process. Don't miss out on this once-in-a-lifetime opportunity to enjoy sun, sand, and sea absolutely free!",
          type: "Spam"
        },
        {
          message: "Hi John, I hope you're doing well. I was wondering if we could reschedule our meeting to 4 PM instead of 3 PM. I have another call that may run a bit longer than expected. Let me know if that works for you. Looking forward to our discussion about the Q2 roadmap. Thanks!",
          type: "Ham"
        },
        {
          message: "This is your last chance to take advantage of our massive clearance sale! Buy one item and get another completely free. From electronics to clothing, everything must go. Act now before our inventory runs out. Click the link and save big on your next shopping spree!",
          type: "Spam"
        },
        {
          message: "Dear Team, Please find attached the quarterly financial report for Q1 2025. The document includes detailed analysis, key performance indicators, and budget adjustments for the upcoming months. If you have any questions or require clarification, feel free to reach out by end of this week.",
          type: "Ham"
        },
        {
          message: "Attention! We've detected unusual activity on your bank account that may indicate unauthorized access. Please verify your account immediately by logging into the secure portal linked below. Failure to act within 24 hours may result in temporary suspension of your services for security reasons.",
          type: "Spam"
        },
        {
          message: "Hey Sarah, Just checking in to see if you'd be free to catch up over coffee this weekend. It’s been a while since we last met and I’d love to hear how everything’s going with your new job. Let me know what day works best for you and we’ll plan something!",
          type: "Ham"
        },
        {
          message: "You have been selected to participate in an exclusive market research study. By completing a quick survey, you stand a chance to win a $1000 Amazon gift card. This offer is only open to the first 100 participants. Click the link below to get started and secure your reward!",
          type: "Spam"
        },
        {
          message: "Hi All, As discussed in today’s meeting, I've compiled and attached the minutes along with key action items for each team. Please review and update your progress by Friday so we can address any blockers in the next sync. Thanks for your active participation!",
          type: "Ham"
        }
      ];

      const getRandomMail = () => {
        const randomIndex = Math.floor(Math.random() * emailSamples.length);
        setInput(emailSamples[randomIndex].message);
      };

    const demoClickHandler = () => {
        if (!isAnalyzing) {
            getRandomMail();
        }
    };

    const AnalyseClickHandler = () => {
        if (input) {
            setIsAnalyzing(true);
            axios
                .post("https://dsbda-mini-project-1s6v.onrender.com/predict", {
                    message: input,
                })
                .then((res) => {
                    console.log(res.data)
                    setIsAnalyzing(false);
                    if (res.data.prediction === "Spam") {
                        setSpamEmail(1);
                        console.log("spammm")
                    } else {
                        setSpamEmail(-1);
                        console.log("no spam")
                    }
                })
                .catch((e) => {
                    console.log(e);
                });
        }
    };

    const shadow = `shadow-[0_1px_12px_rgba(255,255,255,0.5),0_4px_6px_rgba(34,42,53,0.04),0_24px_68px_rgba(47,48,55,0.05),0_2px_3px_rgba(0,0,0,0.04)]`;
    return (
        <motion.div
            initial={{
                opacity: 0,
                scale: 0.98,
                filter: "blur(10px)",
            }}
            animate={{
                opacity: 1,
                scale: 1,
                filter: "blur(0px)",
            }}
            transition={{
                duration: 0.5,
                delay: 0.6,
                ease: "easeInOut",
            }}
            className={` border-purple-900 border-[1px] ${shadow} md:p-10 p-8 rounded-lg`}
        >
            
            <h3 className="text-zinc-100 text-xl sm:text-[25px] md: mb-2">
                <span className="text-red-300 ">Spam</span> Mail Detection
                System
            </h3>
            <hr className="border-zinc-500 my-4" />
            <div className="inputBoxandTitle text-zinc-400">
                <span className="flex justify-between items-center mt-2 sm:mt-8 md:mt-10">
                    <h3 className="text-[13px] mt-2 mb-1">Enter Mail Here</h3>
                    {isAnalyzing ? (
                        <button
                            onClick={() => setIsAnalyzing(false)}
                            className={`bg-red-400 flex justify-center items-center gap-1 px-2 py-[1px] text-[10px] rounded-lg text-white mr-1 transition-opacity duration-700  ${
                                input ? "opacity-100" : "opacity-0"
                            }`}
                        >
                            Stop <RxCross2 />
                        </button>
                    ) : (
                        <button
                            onClick={() => {setInput(""); setSpamEmail(0)}}
                            className={`bg-zinc-200 flex justify-center items-center gap-1 px-2 py-[1px] text-[10px] rounded-lg text-black mr-1 transition-opacity duration-700  ${
                                input ? "opacity-100" : "opacity-0"
                            }`}
                        >
                            clear <MdOutlineClearAll />
                        </button>
                    )}
                </span>
                <div className="w-full">
                    <textarea
                        value={input}
                        disabled={isAnalyzing}
                        onChange={(e) => {setInput(e.target.value); setSpamEmail(0)}}
                        maxLength={500}
                        placeholder=""
                        className="border-zinc-100 border-[1px] rounded-lg py-1 px-2 w-full max-h-[250px] h-16 md:h-20 text-[12px] lg:text-[15px] my-1 md:my-4"
                    />
                    <div className="flex justify-center items-center gap-3">
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
                            onClick={demoClickHandler}
                            className={`bg-pink-800 text-white text-[12px] sm:text-[14px] px-7 py-2 rounded-xl mt-4 flex justify-center items-center gap-2 pl-6 ${shadow} `}
                        >
                            Demo{" "}
                            <motion.span>
                                <MdEmojiObjects />
                            </motion.span>
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
                            onClick={AnalyseClickHandler}
                            className={`${
                                input ? "bg-zinc-200" : "bg-zinc-500"
                            } transition-colors duration-300 text-black text-[12px] sm:text-[14px] px-4 py-2 rounded-xl mt-4 flex justify-center items-center gap-2 pl-6 ${shadow}`}
                        >
                            Analyse{" "}
                            <motion.span
                                className={`rounded-full px-1 py-1 ${
                                    isAnalyzing && "animate-spin"
                                }`}
                            >
                                <BiAnalyse />
                            </motion.span>
                        </motion.button>
                    </div>
                </div>
                <div className="mt-5">
                    {spamEmail === 1 && (
                        <TypewriterEffect
                            words={[
                                {
                                    text: "X",
                                    className: "dark:text-red-500"

                                },
                                {
                                    text: "Spam",
                                    className: "dark:text-red-400",
                                },
                                {
                                    text: "mail",
                                },
                                {
                                    text: "detected",
                                },
                            ]}
                        />
                    )}
                    {spamEmail === -1 &&
                        
                            <TypewriterEffect
                                words={[
                                    {
                                        text: "✅",
                                        
                                    },
                                    {
                                        text: "No",
                                        className:"dark:text-green-200"
                                        
                                    },
                                    {
                                        text: "Spam",
                                        className:"dark:text-green-200"
                                    },
                                    {
                                        text:"Mail"
                                    },
                                    {
                                        text: "detected",
                                    },
                                ]}
                            />
                        
                    }
                    {spamEmail === 0 &&
                        
                        <TypewriterEffect
                            words={[
                                {
                                    text: "Enter",
                                    
                                },
                                {
                                    text: "Mail",
                                },
                                {
                                    text:"and"
                                },
                                {
                                    text: "Click",
                                },
                                {
                                    text: "on",
                                },
                                {
                                    text: "Analyse.",
                                },
                            ]}
                        />
                    
                }
                </div>
            </div>
        </motion.div>
    );
}

export default MainSection;
